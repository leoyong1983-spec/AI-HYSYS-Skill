import csv
import math

MIN_LMTD = 1e-6

def calculate_lmtd(Th_in, Th_out, Tc_in, Tc_out):
    """
    Return the log mean temperature difference of the process.
    """
    delta_T1 = Th_in - Tc_out
    delta_T2 = Th_out - Tc_in
    if delta_T1 <= MIN_LMTD or delta_T2 <= MIN_LMTD:
        if abs(delta_T1 - delta_T2) < MIN_LMTD and delta_T1 > MIN_LMTD:
            return delta_T1
        return MIN_LMTD
    lmtd = (delta_T1 - delta_T2) / math.log(delta_T1 / delta_T2)
    return lmtd

def find_stream_index_by_id(streams_list, stream_id_to_find):
    """
    Return the index of the stream in streams_list whose .id equals stream_id_to_find.
    If no such stream exists, returns -1.
    """
    for index, stream_obj in enumerate(streams_list):
        if stream_obj.id == stream_id_to_find:
            return index
    return -1 # Or raise an error, or return None, if not found

# --- load_data_from_csv function (as previously defined) ---
def load_data_from_csv(streams_filepath, utilities_filepath, matches_U_filepath=None, forbidden_matches=None, requided_matches=None):
    # ... (exact same implementation as before)
    loaded_hot_streams = []
    loaded_cold_streams = []
    loaded_hot_utilities = []
    loaded_cold_utilities = []
    loaded_matches_U = []
    loaded_forbidden_matches = []
    loaded_required_matches = []
    
    try:
        with open(streams_filepath, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row_idx, row in enumerate(reader):
                try:
                    stream_data = {'Name': row['Name'],'Type': row['Type'].lower(),'TIN_spec': float(row['TIN_spec']),'TOUT_spec': float(row['TOUT_spec']),'Fcp': float(row['Fcp'])}
                    if stream_data['Type'] == 'hot': loaded_hot_streams.append(stream_data)
                    elif stream_data['Type'] == 'cold': loaded_cold_streams.append(stream_data)
                    else: print(f"Warning: Unknown stream type '{row['Type']}' for stream '{row['Name']}'. Skipping.")
                except KeyError as e:
                    print(f"Error: Missing column {e} in streams.csv at row {row_idx+1}.")
                    return None,None,None,None,None
                except ValueError as e:
                    print(f"Error: Could not convert value to float in streams.csv at row {row_idx+1} for column {e}.")
                    return None,None,None,None,None
    except FileNotFoundError:
        print(f"Error: Streams file not found at {streams_filepath}")
        return None,None,None,None,None
    except Exception as e:
        print(f"Error reading streams CSV: {e}")
        return None,None,None,None,None
    
    # load matches_U_cost
    if matches_U_filepath:
        try:
            with open(matches_U_filepath, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row_idx, row in enumerate(reader):
                    try:
                        match_U_cost = {'hot': row['Hot_Stream'], 'cold': row['Cold_Stream'], 'U': float(row['U_overall']), 'fix_cost': float(row['Fixed_Cost_Unit']), 'area_cost_coeff': float(row['Area_Cost_Coeff']), 'area_cost_exp': float(row['Area_Cost_Exp'])}
                        loaded_matches_U.append(match_U_cost)
                    except KeyError as e:
                        print(f"Error: Missing column {e} in matches_U_cost.csv at row {row_idx+1}.")
                    except ValueError as e:
                        print(f"Error: Could not convert value to float in matches_U_cost.csv at row {row_idx+1} for column {e}.")
        except FileNotFoundError:
            print(f"Error: matches_U_cost file not found at {matches_U_filepath}")
        except Exception as e:
            print(f"Error reading matches_U_cost CSV: {e}")
    else:
        loaded_matches_U = None
        
    try:
        with open(utilities_filepath, mode='r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row_idx, row in enumerate(reader):
                try:
                    util_data = {'Name': row['Name'],'Type': row['Type'].lower(),'TIN_utility': float(row['TIN_utility']),'TOUT_utility': float(row['TOUT_utility']),'Unit_Cost_Energy': float(row['Unit_Cost_Energy']),'U_overall': float(row['U_overall']),'Fixed_Cost_Unit': float(row['Fixed_Cost_Unit']),'Area_Cost_Coeff': float(row['Area_Cost_Coeff']),'Area_Cost_Exp': float(row['Area_Cost_Exp'])}
                    if util_data['Type'] == 'hot_utility': loaded_hot_utilities.append(util_data)
                    elif util_data['Type'] == 'cold_utility': loaded_cold_utilities.append(util_data)
                    else: print(f"Warning: Unknown utility type '{row['Type']}' for utility '{row['Name']}'. Skipping.")
                except KeyError as e:
                    print(f"Error: Missing column {e} in utilities.csv at row {row_idx+1}.")
                    return None,None,None,None,None
                except ValueError as e:
                    print(f"Error: Could not convert value to float in utilities.csv at row {row_idx+1} for column {e}.")
                    return None,None,None,None,None
    except FileNotFoundError:
        print(f"Error: Utilities file not found at {utilities_filepath}")
        return None,None,None,None,None
    except Exception as e:
        print(f"Error reading utilities CSV: {e}")
        return None,None,None,None,None
    if not loaded_hot_utilities and any(s['Type'] == 'cold' for s in loaded_cold_streams):
        print("Warning: No hot utilities loaded...")
    if not loaded_cold_utilities and any(s['Type'] == 'hot' for s in loaded_hot_streams):
        print("Warning: No cold utilities loaded...")
    
    if forbidden_matches is not None:
        try:
            with open(forbidden_matches, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row_idx, row in enumerate(reader):
                    try:
                        forbidden_match = {'hot': row['Hot_Stream'], 'cold': row['Cold_Stream_Or_Utility']}
                        loaded_forbidden_matches.append(forbidden_match)
                    except KeyError as e:
                        print(f"Error: Missing column {e} in forbidden_matches.csv at row {row_idx+1}.")
                print(f"Loaded {len(loaded_forbidden_matches)} forbidden matches from {forbidden_matches}")
                print(loaded_forbidden_matches)
        except FileNotFoundError:
            print(f"Error: Forbidden matches file not found at {forbidden_matches}")
        
    if requided_matches is not None:
        try:
            with open(requided_matches, mode='r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row_idx, row in enumerate(reader):
                    try:
                        required_match = {'hot': row['Hot_Stream'], 'cold': row['Cold_Stream'], 'min_Q_total': float(row['Min_Q_Total'])}
                        loaded_required_matches.append(required_match)
                    except KeyError as e:
                        print(f"Error: Missing column {e} in required_matches.csv at row {row_idx+1}.")
                print(f"Loaded {len(loaded_required_matches)} required matches from {requided_matches}")
                print(loaded_required_matches)
        except FileNotFoundError:
            print(f"Error: Required matches file not found at {requided_matches}")
        
    return loaded_hot_streams, loaded_cold_streams, loaded_hot_utilities, loaded_cold_utilities, loaded_matches_U, loaded_forbidden_matches, loaded_required_matches
    