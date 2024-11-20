# Password Generator

## Overview

This Python program generates a secure, random password with a customizable length. The password is designed to include a mix of uppercase letters, lowercase letters, digits, and special characters, ensuring strong password security.

## Features

1. **Customizable Length**  
   - Users can specify the desired password length.
   - Passwords can be as short or long as needed (minimum recommended length is 4 for variety).

2. **Character Mix**  
   - Passwords include:
     - Uppercase letters (A-Z)
     - Lowercase letters (a-z)
     - Digits (0-9)
     - Special characters (e.g., `@, #, $, %`)

3. **Randomized Order**  
   - Characters are shuffled to ensure unpredictability.

4. **Secure Randomness**  
   - Uses the `random.choices` method to select characters from respective groups.

## Requirements

- Python 3.x
- Standard Python libraries (`random`, `math`, and `string`)

## How It Works

1. **Input Password Length**  
   - The function `password_generator(length)` takes an integer (`length`) as input, specifying the desired password length.

2. **Calculate Character Counts**  
   - The password is divided into 4 groups:
     - 25% uppercase letters
     - 25% lowercase letters
     - 25% digits
     - Remaining characters as special characters.

3. **Generate Characters**  
   - Randomly selects characters from the respective groups.

4. **Shuffle Characters**  
   - Combines all selected characters and shuffles them to ensure a random order.

5. **Output Password**  
   - Returns the final password as a string.

## Function Explanation

### `password_generator(length)`
Generates a random password with the specified length.

- **Parameters**  
  - `length`: The total number of characters in the password.
- **Returns**  
  - A string containing the randomly generated password.
- **Example Usage**  
  ```python
  print(password_generator(12))  # Output: random 12-character password
  ```

## Example Output

### Input: `password_generator(10)`
```
Output: Q1b@3dG!W#
```

### Input: `password_generator(16)`
```
Output: R3*e$T7q#B8x@M2k
```

## Customization

1. **Adjust Character Ratios**  
   Modify the `num_upper`, `num_lower`, `num_digits`, and `num_special` calculations to alter the distribution of character types.  

2. **Include/Exclude Specific Characters**  
   Modify the `ascii_uppercase`, `ascii_lowercase`, `digits`, or `punctuation` groups in the `random.choices` calls.

## Limitations

- If the password length is less than 4, the generator may fail to include all character types.
- Does not guarantee exact ratios for very short passwords.

## Usage Recommendations

- Use passwords with a length of at least 12 characters for stronger security.
- Avoid reducing the proportion of special characters, as they enhance password strength.
  
## License

This project is open-source and available under the MIT License.
