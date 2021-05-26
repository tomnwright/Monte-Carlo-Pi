import utils

# something wrong, stopping from converging to pi

random_resolution = 10000
max_samples = 1_000_000_000
report_every = 1_000_000


def sample_point():
    x = utils.random_float(-1, 1, random_resolution)
    y = utils.random_float(-1, 1, random_resolution)

    return (x, y)


def in_circle(x, y):
    return pow(x, 2) + pow(y, 2) <= 1


total_in_circle = 0
total_samples = 0
last_reported = 0

while total_samples < max_samples:
    total_samples += 1

    point = sample_point()

    if in_circle(*point):
        total_in_circle += 1

    if total_samples >= last_reported + report_every:
        last_reported = total_samples

        pi_approx = 4 * total_in_circle / total_samples

        print(f"{total_samples} samples;  {utils.pi_accuracy(pi_approx)} digits accuracy;  pi ~= {pi_approx}")
