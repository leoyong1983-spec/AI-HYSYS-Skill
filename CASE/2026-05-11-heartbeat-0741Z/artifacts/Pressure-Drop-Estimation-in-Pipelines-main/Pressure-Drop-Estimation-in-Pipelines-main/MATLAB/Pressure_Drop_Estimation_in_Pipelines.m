disp('=================================================');
disp(' PRESSURE DROP IN A STRAIGHT PIPE ');
disp(' Darcy–Weisbach Method ');
disp('=================================================');

%% =========================
% STAGE 1: USER INPUTS
% =========================
Q   = input('Enter volumetric flow rate Q (m^3/s): ');
D   = input('Enter pipe diameter D (m): ');
L   = input('Enter pipe length L (m): ');

rho = input('Enter fluid density rho (kg/m^3): ');
mu  = input('Enter fluid viscosity mu (Pa.s): ');

eps = input('Enter pipe roughness epsilon (m): ');

nK  = input('Enter number of fittings / minor losses: ');

Ksum = 0;
for i = 1:nK
    Ki = input(['Enter K-value for fitting ', num2str(i), ': ']);
    Ksum = Ksum + Ki;
end

%% =========================
% STAGE 2: VELOCITY & REYNOLDS NUMBER
% =========================
A = pi * D^2 / 4;      % Cross-sectional area (m^2)
v = Q / A;             % Velocity (m/s)

Re = rho * v * D / mu; % Reynolds number

%% =========================
% STAGE 3: FRICTION FACTOR
% =========================
if Re < 2300
    flowRegime = 'Laminar Flow';
    f = 64 / Re;

else
    flowRegime = 'Turbulent Flow';

    disp(' ');
    disp('Select friction factor method:');
    disp('1 → Swamee–Jain (Explicit)');
    disp('2 → Colebrook (Iterative)');
    method = input('Enter choice (1 or 2): ');

    if method == 1
        % Swamee–Jain equation
        f = 0.25 / ...
            ( log10( eps/(3.7*D) + 5.74/(Re^0.9) ) )^2;
    else
        % Colebrook equation
        f = colebrook(Re, eps, D);
    end
end

%% =========================
% STAGE 4: FRICTIONAL PRESSURE DROP
% =========================
dp_friction = f * (L/D) * (rho * v^2 / 2);

%% =========================
% STAGE 5: MINOR LOSSES
% =========================
dp_minor = Ksum * (rho * v^2 / 2);

%% =========================
% TOTAL PRESSURE DROP
% =========================
dp_total = dp_friction + dp_minor;

%% =========================
% DISPLAY RESULTS
% =========================
disp(' ');
disp('================ RESULTS ================');
fprintf('Flow regime            : %s\n', flowRegime);
fprintf('Velocity (m/s)         : %.4f\n', v);
fprintf('Reynolds number        : %.3e\n', Re);
fprintf('Friction factor (f)    : %.5f\n', f);
fprintf('Δp (friction) (Pa)     : %.2f\n', dp_friction);
fprintf('Δp (minor) (Pa)        : %.2f\n', dp_minor);
fprintf('Δp (total) (Pa)        : %.2f\n', dp_total);
disp('=========================================');

%% =========================
% COLEBROOK FUNCTION
% =========================
function f = colebrook(Re, eps, D)
% Solves Colebrook equation using iteration

f = 0.02;      % Initial guess
tol = 1e-6;

for i = 1:100
    f_new = 1 / ...
        ( -2 * log10( eps/(3.7*D) + 2.51/(Re*sqrt(f)) ) )^2;

    if abs(f_new - f) < tol
        break;
    end

    f = f_new;
end
end
