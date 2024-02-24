#include "..\LibLW1\Header.h"

int main() {
    setlocale(LC_ALL, "rus");
    cout << "ввидите первое число в десятичном формати\n";
    int a;
    cin >> a;
    displayInfo(a);
    cout << "ввидите втарое чисьло в десятичнам фармати\n";
    int b;
    cin >> b;
    displayInfo(b);

operations:
    cout << "выбирьте опирацыю каторую хотице правести:\n 1. сълажение чисель в дапалнительном коде.\n 2. вычитанье в дполнительнам коде\n 3. умножць числа в допалнительном коди\n 4. диленье чисель в прямом коди\n 5. скадванье чисель по стандарту IEEE-754-2008\n ";
    char temp;
    cin >> temp;
    if (temp == '1') {
        vector<int> ans = addAdditional(a, b);
        cout << "слажение " << a << " и " << b << ": ";
        for (int temp : ans) cout << temp;
        cout << endl;
        int c = a + b;
        displayInfo(c);
    }
    else if (temp == '2') {
        vector<int> substractedBin = subtractBinary(a, b);
        cout << "вычитанье " << a << " и " << b << ": ";
        for (int temp : substractedBin) cout << temp;
        cout << endl;
        int c = a - b;
        displayInfo(c);


    }
    else if (temp == '3') {
        vector<int> multipBin = multiplyBinary(a, b);
        cout << "умнаженье " << a << " и " << b << ": ";
        for (int temp : multipBin) cout << temp;
        cout << endl;
        int c = a * b;
        displayInfo(c);
    }
    else if (temp == '4') {
        vector<int> devidedBin = divideBinary(12, 2);
        for (int temp : devidedBin) cout << temp;
        cout << endl;
        int c = a / b;
        displayInfo(c);
    }
    else if (temp == '5') {
        float c;
        float d;
        cout << "введите 2 числа с плавающей точкой ";
        cin >> c >> d;
        vector<int> binaryA = floatToBinary(c);
        vector<int> binaryB = floatToBinary(d);
        cout << "Binary A: ";
        for (int bit : binaryA) {
            cout << bit;
        }
        cout << std::endl;

        cout << "Binary B: ";
        for (int bit : binaryB) {
            cout << bit;
        }
        cout << std::endl;
        vector<int> result = addFloat(binaryA, binaryB);
        cout << "результат сложения чисель " << c << " и " << d << " по стондарту IEEE-754-2008: ";
        for (int temp : result) {
            cout << temp;
        }
        cout << endl;
    }
    else return 1;

    goto operations;
    return 0;
}
