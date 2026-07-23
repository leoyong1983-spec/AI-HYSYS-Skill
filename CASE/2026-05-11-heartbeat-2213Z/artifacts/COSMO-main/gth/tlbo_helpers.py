import copy
import numpy as np
import random
from .ga_helpers import GeneticAlgorithmHEN
from .hen_models import HENProblem

# --- Teaching-Learning-Based Optimization for HEN Synthesis ---
class TeachingLearningBasedOptimizationHEN:
    def __init__(self, problem,
                 population_size,
                 generations,
                 random_seed=None,
                 utility_cost_factor=1.0,
                 pinch_deviation_penalty_factor=0.0,
                 sws_max_iter=50,
                 sws_conv_tol=0.001):
        self.problem: HENProblem = problem
        self.population_size = population_size
        self.generations = generations
        self.random_seed = random_seed
        self.utility_cost_factor = utility_cost_factor
        self.pinch_deviation_penalty_factor = pinch_deviation_penalty_factor
        self.sws_max_iter = sws_max_iter
        self.sws_conv_tol = sws_conv_tol

        if random_seed is not None:
            random.seed(random_seed)
            np.random.seed(random_seed)

        # Chromosome segment lengths (same as GA)
        self.len_Z = self.problem.NH * self.problem.NC * self.problem.num_stages
        self.len_R_hot_splits = self.problem.NH * self.problem.num_stages * self.problem.NC
        self.len_R_cold_splits = self.problem.NC * self.problem.num_stages * self.problem.NH
        self.chromosome_length = self.len_Z + self.len_R_hot_splits + self.len_R_cold_splits

        self.population = []

    def _initialize_population(self):
        self.population = []
        for _ in range(self.population_size):
            self.population.append(self._create_random_full_chromosome())

    def _create_random_full_chromosome(self):
        # Resue from GeneticAlgorithmHEN
        return GeneticAlgorithmHEN._create_random_full_chromosome(self)

    def _decode_chromosome(self, chromosome):
        # Reuse from HENProblem
        return self.problem._decode_chromosome(chromosome)

    def _calculate_fitness(self, chromosome):
        # Reuse from GeneticAlgorithmHEN
        return GeneticAlgorithmHEN._calculate_fitness(self, chromosome)

    def run(self, run_id_for_print=""):
        if self.random_seed is not None:
            random.seed(self.random_seed)
            np.random.seed(self.random_seed)

        self._initialize_population()
        population = [chromo.copy() for chromo in self.population]
        best_chromosome_overall = None
        best_costs_overall_dict = {"TAC_GA_optimizing": float('inf'), "TAC_true_report": float('inf')}
        best_details_overall = None
        print_prefix = f"Run {run_id_for_print} - " if run_id_for_print else ""
        log_best_true_tac_per_gen = []
        log_avg_true_tac_per_gen = []
        log_best_ga_tac_per_gen = []
        log_avg_ga_tac_per_gen = []
        for gen in range(self.generations):
            # Evaluate all learners
            fitnesses = []
            details_list = []
            for chromo in population:
                try:
                    costs_dict, details = self._calculate_fitness(chromo)
                    fitnesses.append(costs_dict)
                    details_list.append(details)
                except Exception as e:
                    error_costs = {"TAC_GA_optimizing": float('inf'), "TAC_true_report": float('inf')}
                    fitnesses.append(error_costs)
                    details_list.append([])
            # Teacher: best (min) TAC_GA_optimizing
            best_idx = int(np.argmin([c['TAC_GA_optimizing'] for c in fitnesses]))
            teacher = population[best_idx].copy()
            teacher_fitness = fitnesses[best_idx]['TAC_GA_optimizing']
            # Mean learner vector
            X_mean = np.mean(np.stack(population), axis=0)
            # Teacher Phase
            new_population = []
            for i, X_old in enumerate(population):
                r = np.random.uniform(0, 1, size=X_old.shape)
                TF = np.random.choice([1, 2])
                X_teacher = teacher
                X_new = X_old + r * (X_teacher - TF * X_mean)
                # Enforce constraints:
                # Z part: binary
                X_new[:self.len_Z] = (X_new[:self.len_Z] >= 0.5).astype(int)
                # R parts: positive, minimum 1e-6
                X_new[self.len_Z:self.len_Z + self.len_R_hot_splits] = np.clip(
                    X_new[self.len_Z:self.len_Z + self.len_R_hot_splits], 1e-6, None
                )
                X_new[self.len_Z + self.len_R_hot_splits:] = np.clip(
                    X_new[self.len_Z + self.len_R_hot_splits:], 1e-6, None
                )
                # Evaluate new
                try:
                    new_costs, new_details = self._calculate_fitness(X_new)
                except Exception as e:
                    new_costs = {"TAC_GA_optimizing": float('inf'), "TAC_true_report": float('inf')}
                    new_details = []
                # Accept if better
                if new_costs['TAC_GA_optimizing'] < fitnesses[i]['TAC_GA_optimizing']:
                    new_population.append(X_new)
                    fitnesses[i] = new_costs
                    details_list[i] = new_details
                else:
                    new_population.append(X_old)
            population = new_population
            # Learner Phase
            for i, Xi in enumerate(population):
                idxs = list(range(self.population_size))
                idxs.remove(i)
                j = random.choice(idxs)
                Xj = population[j]
                fi = fitnesses[i]['TAC_GA_optimizing']
                fj = fitnesses[j]['TAC_GA_optimizing']
                r = np.random.uniform(0, 1, size=Xi.shape)
                if fi < fj:
                    Xi_new = Xi + r * (Xi - Xj)
                else:
                    Xi_new = Xi + r * (Xj - Xi)
                # Enforce constraints:
                Xi_new[:self.len_Z] = (Xi_new[:self.len_Z] >= 0.5).astype(int)
                Xi_new[self.len_Z:self.len_Z + self.len_R_hot_splits] = np.clip(
                    Xi_new[self.len_Z:self.len_Z + self.len_R_hot_splits], 1e-6, None
                )
                Xi_new[self.len_Z + self.len_R_hot_splits:] = np.clip(
                    Xi_new[self.len_Z + self.len_R_hot_splits:], 1e-6, None
                )
                try:
                    new_costs, new_details = self._calculate_fitness(Xi_new)
                except Exception as e:
                    new_costs = {"TAC_GA_optimizing": float('inf'), "TAC_true_report": float('inf')}
                    new_details = []
                if new_costs['TAC_GA_optimizing'] < fitnesses[i]['TAC_GA_optimizing']:
                    population[i] = Xi_new
                    fitnesses[i] = new_costs
                    details_list[i] = new_details
            # Track best
            best_idx = int(np.argmin([c['TAC_GA_optimizing'] for c in fitnesses]))
            best_ga_tac_this_gen = fitnesses[best_idx]['TAC_GA_optimizing']
            best_true_tac_this_gen = fitnesses[best_idx]['TAC_true_report']
            if best_ga_tac_this_gen < best_costs_overall_dict['TAC_GA_optimizing']:
                best_costs_overall_dict = copy.deepcopy(fitnesses[best_idx])
                best_chromosome_overall = population[best_idx].copy()
                best_details_overall = details_list[best_idx]
            gen_true_tacs = [c['TAC_true_report'] for c in fitnesses]
            gen_ga_tacs = [c['TAC_GA_optimizing'] for c in fitnesses]
            avg_true_tac_this_gen = np.mean(gen_true_tacs) if gen_true_tacs else float('inf')
            avg_ga_tac_this_gen = np.mean(gen_ga_tacs) if gen_ga_tacs else float('inf')
            log_best_true_tac_per_gen.append(best_costs_overall_dict['TAC_true_report'])
            log_avg_true_tac_per_gen.append(avg_true_tac_this_gen)
            log_best_ga_tac_per_gen.append(best_costs_overall_dict['TAC_GA_optimizing'])
            log_avg_ga_tac_per_gen.append(avg_ga_tac_this_gen)
            overall_best_true_str = f"{best_costs_overall_dict['TAC_true_report']:.2f}" if best_costs_overall_dict['TAC_true_report']!=float('inf') else "Inf"
            overall_best_ga_str = f"{best_costs_overall_dict['TAC_GA_optimizing']:.2f}" if best_costs_overall_dict['TAC_GA_optimizing']!=float('inf') else "Inf"
            print(f"{print_prefix}Gen {gen+1:03d}/{self.generations} - Best True TAC (Overall): {overall_best_true_str}, Best GA TAC (Overall): {overall_best_ga_str}")
        return best_chromosome_overall, best_costs_overall_dict, best_details_overall