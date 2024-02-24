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

// ������� ��� ���������� ��������� ����
vector<int> findOnesComplement(int n) {
    vector<int> arr = decimalToBinary(n);
    if (arr[0] == 1) {
        for (size_t i = 1; i <= 7; ++i) {
            arr[i] == 1 ? arr[i] = 0 : arr[i] = 1;
        }
    }
    return arr;
}

// ������� ��� ���������� ��������������� ����
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

// ������� ��� ������ ��������� ����
void printBinary(std::vector<int>& binary) {
    for (int i = 0; i < binary.size(); i++)
        std::cout << binary[i];
}

// ������� ��� �������� ���� ����� � �������������� ����
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

// ������� ��� ��������� ���� ����� � �������������� ����
vector<int> subtractBinary(int a, int b) {
    b -= 2 * b;
    vector<int> ans = addAdditional(a, b);
    return ans;
}

// ������� ��� ��������� ���� �����
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

// ������� ��� ������� ���� �����
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

vector<int> addFloat(const std::vector<int>& a, const std::vector<int>& b) {
    std::vector<int> result(32);

    bool sequenceEquals = true;

    // ���������, ����� �� ���� ����� �����
    for (int i = 1; i < 32; i++) {
        if (a[i] != b[i]) {
            sequenceEquals = false;
            break;
        }
    }

    // ���� ����� ���������, ��������� ����� ����
    if (sequenceEquals) {
        return std::vector<int>(32, 0);
    }

    int exponent1 = 0;
    int exponent2 = 0;
    int mantissa1 = 0;
    int mantissa2 = 0;

    // ��������� ���������� � �������� �� ������� ��������
    for (int i = 1; i <= 8; i++) {
        exponent1 |= a[i] ? (1 << (8 - i)) : 0;
        exponent2 |= b[i] ? (1 << (8 - i)) : 0;
    }

    for (int i = 9; i <= 31; i++) {
        mantissa1 |= a[i] ? (1 << (31 - i)) : 0;
        mantissa2 |= b[i] ? (1 << (31 - i)) : 0;
    }

    mantissa1 |= 1 << 23; // ��������� ������� ���
    mantissa2 |= 1 << 23;

    int resultExponent = std::max(exponent1, exponent2);

    // �������� ��������, ���� ��� ����������
    mantissa1 >>= resultExponent - exponent1;
    mantissa2 >>= resultExponent - exponent2;

    int resultMantissa = (a[0] ? -mantissa1 : mantissa1) + (b[0] ? -mantissa2 : mantissa2);

    if (resultMantissa < 0) {
        result[0] = true;
        resultMantissa = -resultMantissa;
    }

    // ����������� ��������
    while (resultMantissa >= (1 << 23)) {
        resultMantissa >>= 1;
        resultExponent++;
    }

    // ���� �������� �� �������, ������� �� �� �������
    if (resultMantissa != 0) {
        while (resultMantissa < (1 << 23)) {
            resultMantissa <<= 1;
            resultExponent--;
        }
    }

    // ���������� ��������� � �������������� ������� ������
    for (int i = 1; i <= 8; i++) {
        result[i] = (resultExponent >> (8 - i)) & 1;
    }

    // ���������� �������� � �������������� ������� ������
    for (int i = 9; i <= 31; i++) {
        result[i] = (resultMantissa >> (31 - i)) & 1;
    }

    return result;
}



void displayInfo(int a) {
    vector<int> bin = decimalToBinary(a);
    cout << "������ ��� ����� " << a << ": ";
    for (size_t i = 0; i < bin.size(); ++i)
        cout << bin[i]; 
    cout << endl;
    vector<int> reversedA = findOnesComplement(a);
    cout << "�������� ��� ����� " << a << ": ";
    for (size_t i = 0; i < reversedA.size(); ++i)
        cout << reversedA[i];
    cout << endl;
    vector<int> additionalA = findTwosComplement(a);
    cout << "�������������� ��� ����� " << a << ": ";
    for (size_t i = 0; i < additionalA.size(); ++i)
        cout << additionalA[i];
    cout << endl;
}

float binaryToFloat(const std::vector<int>& bits) {
    // �������� ����
    int sign = bits[0] ? -1 : 1;

    // �������� ����������
    int exponent = 0;
    for (int i = 1; i <= 8; i++) {
        exponent |= bits[i] ? (1 << (8 - i)) : 0;
    }
    exponent -= 127; // ������������ ��������

    // �������� ��������
    float mantissa = 1.0f;
    for (int i = 9; i <= 31; i++) {
        mantissa += bits[i] ? (1.0f / (1 << (i - 8))) : 0.0f;
    }

    // ������������ ����������� ������
    if (exponent == -127 && mantissa == 0.0f) {
        return 0.0f; // ���������� ����
    }
    else if (exponent == 128 && mantissa == 0.0f) {
        return sign * std::numeric_limits<float>::infinity(); // ���������� �������������
    }
    else if (exponent == 128 && mantissa != 0.0f) {
        return std::numeric_limits<float>::quiet_NaN(); // ���������� NaN
    }

    // ���������� �������� ��������
    return sign * std::pow(2, exponent) * mantissa;
}