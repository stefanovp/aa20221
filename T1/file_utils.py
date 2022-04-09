class AAFileUtils:
    def load_test_subjects(file_path):
        
        current_set = None
        test_data = {}
        with open(file_path) as file:
            for line in file:
                if not line[0].isnumeric():
                    current_set = line
                    test_data[current_set] = []
                else:
                    if(current_set != None):
                        test_data[current_set].append(int(line))

        return test_data
