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

// Функция для нахождения обратного кода
vector<int> findOnesComplement(int n) {
    vector<int> arr = decimalToBinary(n);
    if (arr[0] == 1) {
        for (size_t i = 1; i <= 7; ++i) {
            arr[i] == 1 ? arr[i] = 0 : arr[i] = 1;
        }
    }
    return arr;
}

// Функция для нахождения дополнительного кода
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

// Функция для вывода двоичного кода
void printBinary(std::vector<int>& binary) {
    for (int i = 0; i < binary.size(); i++)
        std::cout << binary[i];
}

// Функция для сложения двух чисел в дополнительном коде
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

// Функция для вычитания двух чисел в дополнительном коде
vector<int> subtractBinary(int a, int b) {
    b -= 2 * b;
    vector<int> ans = addAdditional(a, b);
    return ans;
}

// Функция для умножения двух чисел
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

// Функция для деления двух чисел
vector<int> divideBinary(int a, int b) {
    vector<int> num1 = decimalToBinary(a);
    vector<int> num2 = decimalToBinary(b);
    vector<int> result(8);
    int decimal1 = 0, decimal2 = 0;
    for (int i = 1; i < 8; ++i) {
        decimal1 += num1[i] * pow(2, 7 - i);
        decimal2 += num2[i] * pow(2, 7 - i);
    }
    if (decimal2 != 0) {
        int quotient = decimal1 / decimal2;
        result = decimalToBinary(quotient);
    }
    else {
        cout << "Error: Division by zero" << endl;
    }
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

std::vector<int> addFloat(const std::vector<int>& a, const std::vector<int>& b) {
    std::vector<int> result(32);
    std::vector<int> exponentA(8), exponentB(8);
    std::vector<int> mantissaA(23), mantissaB(23);
    for (int i = 1; i <= 8; ++i) {
        exponentA[i - 1] = a[i];
        exponentB[i - 1] = b[i];
    }
    for (int i = 9; i < 32; ++i) {
        mantissaA[i - 9] = a[i];
        mantissaB[i - 9] = b[i];
    }
    int expA = 0, expB = 0;
    for (int i = 0; i < 8; ++i) {
        expA += exponentA[i] * std::pow(2, 7 - i);
        expB += exponentB[i] * std::pow(2, 7 - i);
    }
    float mantA = 1.0, mantB = 1.0;
    for (int i = 0; i < 23; ++i) {
        mantA += mantissaA[i] * std::pow(2, -1 - i);
        mantB += mantissaB[i] * std::pow(2, -1 - i);
    }
    int diffExp = std::abs(expA - expB);
    if (expA > expB) {
        mantB /= std::pow(2, diffExp);
        expB = expA;
    }
    else {
        mantA /= std::pow(2, diffExp);
        expA = expB;
    }
    float resultMantissa = 0;
    if (expA == 0 && expB == 0) {
        resultMantissa = mantA + mantB;
    }
    else {
        mantA += 1;
        mantB += 1;
        resultMantissa = mantA + mantB;
    }
    if (resultMantissa >= 2) {
        resultMantissa /= 2;
        expA++;
    }
    int resultExponent = expA;
    for (int i = 0; i < 8; ++i) {
        result[i + 1] = resultExponent % 2;
        resultExponent /= 2;
    }
    for (int i = 0; i < 23; ++i) {
        result[9 + i] = static_cast<int>(resultMantissa) % 2;
        resultMantissa -= static_cast<int>(resultMantissa);
        resultMantissa *= 2;
    }
    return result;
}

void displayInfo(int a) {
    vector<int> bin = decimalToBinary(a);
    cout << "прямой код чисьла " << a << ": ";
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