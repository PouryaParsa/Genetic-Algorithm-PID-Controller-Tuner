import random
import csv
import os

class Map:
    def __init__(self, config):
        file_path = os.path.join(config.data_directory, config.map_filename)
        if config.new_map:
            self.create_new(file_path, config.max_timesteps, config.line_smoothness)
        else:
            self.load(file_path)

    def create_new(self, file_path, max_timesteps, line_smoothness):
        random.seed()
        map_values = [0]

        with open(file_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for time in range(1, max_timesteps):
                if random.random() < line_smoothness:
                    new_value = map_values[-1] + (random.random() - 0.5) / 1000
                else:
                    new_value = map_values[-1]
                map_values.append(new_value)
                csv_writer.writerow([new_value])

        self.map = map_values

    def load(self, file_path):
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            map_values = [float(row[0]) for row in csv_reader]

        self.map = map_values

    def get(self, index):
        return self.map[index]
