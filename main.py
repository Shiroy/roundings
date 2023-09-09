import numpy as np

def analyse_rounding(rounded, samples):
    errors = rounded - samples
    return (
        np.round(np.mean(errors), 2), 
        np.round(np.std(errors), 2),
        np.round(np.percentile(errors, 25), 2),
        np.round(np.percentile(errors, 75), 2),
        np.round(np.sum(errors), 2)
    )

def school_rounding_imp(dec, rem):
    if(np.isclose(rem, 0.5)):
        return dec+1
    elif(rem > 0.5):
        return dec+1
    else:
        return dec

school_rounding = np.frompyfunc(school_rounding_imp, 2, 1)

def main():
    samples = np.arange(0, 1000, 0.05)
    floored = np.floor(samples)
    ceiled = np.ceil(samples)
    bank_rounded = np.round(samples, 0)

    (int_part, float_part) = np.divmod(samples, 1)
    school_rounding_res = school_rounding(int_part, float_part)

    (floored_mean, floored_std, floored_q1, floored_q3, floored_acc_error) = analyse_rounding(floored, samples)
    (ceiled_mean, ceiled_std, ceiled_q1, ceiled_q3, ceiled_acc_error) = analyse_rounding(ceiled, samples)
    (banker_mean, banker_std, banker_q1, banker_q3, banker_acc_error) = analyse_rounding(bank_rounded, samples)
    (school_mean, school_std, school_q1, school_q3, school_acc_error) = analyse_rounding(school_rounding_res, samples)

    print(f"Floor - Error mean = {floored_mean} ; Deviation = {floored_std} ; P25 = {floored_q1} ; P75 = {floored_q3} ; Acc err = {floored_acc_error}")
    print(f"Ceiled - Error mean = {ceiled_mean} ; Deviation = {ceiled_std} ; P25 = {ceiled_q1} ; P75 = {ceiled_q3} ; Acc err = {ceiled_acc_error}")
    print(f"School - Error mean = {school_mean} ; Deviation = {school_std} ; P25 = {school_q1} ; P75 = {school_q3} ; Acc err = {school_acc_error}")
    print(f"Banker - Error mean = {banker_mean} ; Deviation = {banker_std} ; P25 = {banker_q1} ; P75 = {banker_q3} ; Acc err = {banker_acc_error}")

if __name__ == "__main__":
    main()