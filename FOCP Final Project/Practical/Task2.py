import sys

def process_line(line):
    parts = line.split(",")
    if len(parts) == 3:
        try:
            cat_type, entry_time, exit_time = parts
            return cat_type, int(entry_time), int(exit_time)
        except ValueError:
            return None

def analyze_log(file_path):
    with open(file_path, "r") as f:
        cat_visits = other_cats = total_time = 0
        durations = []

        for line in f:
            data = process_line(line.strip())
            if data:
                cat_type, entry, exit = data
                if cat_type == "OURS":
                    cat_visits += 1
                    total_time += exit - entry
                    durations.append(exit - entry)
                else:
                    other_cats += 1

        hours, minutes = divmod(total_time, 60)
        average_duration = sum(durations) / len(durations) if durations else 0
        longest_visit = max(durations) if durations else 0
        shortest_visit = min(durations) if durations else 0

        print("Log File Analysis")
        print("==================")
        print("Cat Visits:", cat_visits)
        print("Other Cats:", other_cats)
        print("Total Time in House:", hours, "Hours,", minutes, "Minutes")
        print("Average Visit Length:", average_duration, "Minutes")
        print("Longest Visit:", longest_visit, "Minutes")
        print("Shortest Visit:", shortest_visit, "Minutes")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cat_shelter.py <log_file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    analyze_log(file_path)
