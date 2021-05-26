import random

# first 50 actual digits of pi
pi_digits = "14159265358979323846264338327950288419716939937510"


def pi_accuracy(estimate):
    """
    Determine how many digits estimate of pi is accurate to
    :param estimate: estimate for pi
    :return: number of digits estimate accurate to
    """
    digits = str(float(estimate)).split(".")[1]
    assert len(digits) < 50

    for e, d in enumerate(digits):
        if d != pi_digits[e]:
            return e

    # all digits are accurate
    return len(digits)


def random_float(range_min, range_max, resolution):
    sample = random.randint(0, resolution)
    return range_min + sample * (range_max - range_min) / resolution


if __name__ == '__main__':

    print(random_float(-1,1,1000000))
    print(pi_accuracy(3.14159525))
