#include "Header.h"

vector<int> decimalToBinary(int n) {
    vector<int> binary(8);
    int i = 7;
    (n > 0) ? binary[0] = 0 : binary[0] = 1;
    do
    {
        binary[i] = abs(n) % 2;
        n /= 2;
        i--;
    } while (abs(n) > 0);
    return binary;
}

vector<int> findOnesComplement(int n) {
    vector<int> arr = decimalToBinary(n);
    if (arr[0] == 1) {
        for (size_t i = 1; i <= 7; ++i) {
            arr[i] == 1 ? arr[i] = 0 : arr[i] = 1;
        }
    }
    return arr;
}

vector<int> findTwosComplement(int n) {
    if (n > 0) {
        vector<int> arr = decimalToBinary(n);
        return arr;
    }
    vector<int> arr = findOnesComplement(n);
    int cary = 0;
    if (arr[0] == 1) {
        arr[7] = arr[7] + 1;
        if (arr[7] > 1) {
            arr[7] = arr[7] % 2;
            cary = 1;
        }
        for (int i = arr.size() - 2; i >= 0; --i) {
            arr[i] = arr[i] + cary;
            cary = 0;
            if (arr[i] > 1) {
                arr[i] = arr[i] % 2;
                cary = 1;
            }
            else return arr;
        }
    }
    return arr;
}

void printBinary(std::vector<int>& binary) {
    for (int i = 0; i < binary.size(); i++)
        std::cout << binary[i];
}

vector<int> addAdditional(int a, int b) {
    vector<int> additionalA = findTwosComplement(a);
    vector<int> additionalB = findTwosComplement(b);
    vector<int> ans(8);
    int cary = 0;
    for (int i = additionalA.size() - 1; i >= 0; --i) {
        ans[i] = additionalA[i] + additionalB[i] + cary;
        cary = 0;
        if (ans[i] > 1) {
            ans[i] = ans[i] % 2;
            cary = 1;
        }
    }
    return ans;
}

vector<int> subtractBinary(int a, int b) {
    b -= 2 * b;
    vector<int> ans = addAdditional(a, b);
    return ans;
}

vector<int> multiplyBinary(int a, int b) {
    vector<int> binA = decimalToBinary(a);
    vector<int> binB = decimalToBinary(b);
    vector<int> ans(binA.size() + binB.size() - 1);
    for (int i = binA.size() - 1; i >= 0; --i) {
        for (int j = binB.size() - 1; j >= 0; --j) {
            ans[i + j] += (binA[j] != 0 && binB[i] != 0);
        }
    }
    ans.erase(ans.begin(), ans.begin() + 7);

    int cary = 0;
    for (int i = ans.size() - 1; i >= 0; --i) {
        ans[i] += cary;
        cary = 0;
        if (ans[i] > 1) {
            ans[i] = ans[i] % 2;
            cary = 1;
        }
    }
    return ans;
}

vector<string> divideBinary(int a, int b) {
    vector<string> result(8);
    vector<int> num1 = decimalToBinary(a);
    vector<int> num2 = decimalToBinary(b);
    int decimal1 = 0, decimal2 = 0;

    for (int i = 0; i < 8; ++i) {
        decimal1 += num1[i] * pow(2, 7 - i);
        decimal2 += num2[i] * pow(2, 7 - i);
    }

    if (decimal2 == 0) {
        throw invalid_argument("Error: Division by zero");
    }

    double quotient = static_cast<double>(decimal1) / decimal2;

    int intPart = static_cast<int>(quotient);
    string binaryIntPart = "";
    while (intPart > 0) {
        binaryIntPart = to_string(intPart % 2) + binaryIntPart;
        intPart /= 2;
    }
    if (binaryIntPart == "") {
        binaryIntPart = "0";
    }

    string binaryFractionalPart = ".";
    quotient -= static_cast<int>(quotient);
    for (int i = 0; i < 5; ++i) {
        quotient *= 2;
        binaryFractionalPart += to_string(static_cast<int>(quotient));
        quotient -= static_cast<int>(quotient);
    }

    result[0] = binaryIntPart + binaryFractionalPart;
    return result;
}

std::vector<int> floatToBinary(float value) {
    std::vector<int> bits(32);

    if (value == 0) {
        return bits;
    }

    bits[0] = value < 0;

    int exponent = 0;
    float mantissa = std::abs(value);

    while (mantissa >= 2) {
        mantissa /= 2;
        exponent++;
    }
    while (mantissa < 1) {
        mantissa *= 2;
        exponent--;
    }
    mantissa -= 1;
    exponent += 127;

    for (int i = 1; i < 9; i++) {
        bits[i] = (exponent >> (8 - i) & 1) == 1;
    }

    for (int i = 0; i < 23; i++) {
        mantissa *= 2;

        if (mantissa >= 1) {
            bits[i + 9] = true;
            mantissa--;
        }
    }

    return bits;
}

vector<bool> BinaryFloat(float value) {
    std::vector<bool> bits(32);

    if (value == 0) {
        return bits;
    }

    bits[0] = value < 0;

    int exponent = 0;
    float mantissa = std::abs(value);

    while (mantissa >= 2) {
        mantissa /= 2;
        exponent++;
    }
    while (mantissa < 1) {
        mantissa *= 2;
        exponent--;
    }
    mantissa -= 1;
    exponent += 127;

    for (int i = 1; i < 9; i++) {
        bits[i] = (exponent >> (8 - i) & 1) == 1;
    }

    for (int i = 0; i < 23; i++) {
        mantissa *= 2;

        if (mantissa >= 1) {
            bits[i + 9] = true;
            mantissa--;
        }
    }

    return bits;
}

std::vector<int> addFloat(const std::vector<int>& a, const std::vector<int>& b) {
    std::vector<int> result(32);

    int carry = 0;
    for (int i = 31; i >= 0; i--) {
        int sum = a[i] + b[i] + carry;
        result[i] = sum % 2;
        carry = sum / 2;
    }

    return result;
}



void displayInfo(int a) {
    vector<int> bin = decimalToBinary(a);
    cout << "прямой код числа " << a << ": ";
    for (size_t i = 0; i < bin.size(); ++i)
        cout << bin[i]; 
    cout << endl;
    vector<int> reversedA = findOnesComplement(a);
    cout << "обратный код числа " << a << ": ";
    for (size_t i = 0; i < reversedA.size(); ++i)
        cout << reversedA[i];
    cout << endl;
    vector<int> additionalA = findTwosComplement(a);
    cout << "даполнитильный код числа " << a << ": ";
    for (size_t i = 0; i < additionalA.size(); ++i)
        cout << additionalA[i];
    cout << endl;
}

float binaryToFloat(const std::vector<int>& bits) {
    int sign = bits[0] ? -1 : 1;
    int exponent = 0;
    for (int i = 1; i <= 8; i++) {
        exponent |= bits[i] ? (1 << (8 - i)) : 0;
    }
    exponent -= 127;

    float mantissa = 1.0f;
    for (int i = 9; i <= 31; i++) {
        mantissa += bits[i] ? (1.0f / (1 << (i - 8))) : 0.0f;
    }

    if (exponent == -127 && mantissa == 0.0f) {
        return 0.0f;
    }
    else if (exponent == 128 && mantissa == 0.0f) {
        return sign * std::numeric_limits<float>::infinity();
    }
    else if (exponent == 128 && mantissa != 0.0f) {
        return std::numeric_limits<float>::quiet_NaN();

        return sign * std::pow(2, exponent) * mantissa;
    }
    return 0;
}

void displayInfo(float f) {
    string bin = floattoBinary(f);
    cout << "бинарный вид чисьла " << f << ": ";
    cout << bin;
    cout << endl;
    cout << "прямой код чисьла " << f << ": ";
    cout << bin;
    cout << endl;
    cout << "обратный код чисьла " << f << ": ";
    cout << bin;
    cout << endl;
}

string floattoBinary(float f) {
    string temp = to_string(f);
    int n = stoi(temp.substr(0, temp.find('.')));
    string binary = "0000000000000";
    (f > 0) ? binary += '0' : binary += '1';
    int i = 7;

    while (n > 0) {
        binary[i] = (n % 2) + '0';
        n /= 2;
        i--;
    }
    binary[8] = '.';
    i = 9;
    float decimalPart = abs(f - (int)f);
    for (int j = 0; j < 5; ++j) {
        decimalPart *= 2;
        binary[i] = (int(decimalPart)) + '0';
        decimalPart -= int(decimalPart);
        i++;
    }

    return binary;
}
