#include "..\LibLW1\Header.h"

int main() {
    setlocale(LC_ALL, "rus");
    cout << "введите первое число в десятичном формате\n";
    int a;
    cin >> a;
    displayInfo(a);
    cout << "ввидите второе чисьло в десятичнам фармати\n";
    int b;
    cin >> b;
    displayInfo(b);

operations:
    cout << "выбиртьте опирацию каторую хотите2е проварвести:\n 1. слажение чисел в двыапалнительном коде.\n 2. вычитанк1е в дполнительнам коде\n 3. умножыть) числа в допалнительном коди\n 4. диленье чисел в прямом коди\n 5. скадвакцнье чисел по стандарту IEEE-754-2008\n ";
    char temp;
    cin >> temp;
    if (temp == '1') {
        vector<int> ans = addAdditional(a, b);
        cout << "сложение " << a << " и " << b << ": ";
        for (int temp : ans) cout << temp;
        cout << endl;
        int c = a + b;
        displayInfo(c);
    }
    else if (temp == '2') {
        vector<int> substractedBin = subtractBinary(a, b);
        cout << "вычитанье4е " << a << " и " << b << ": ";
        for (int temp : substractedBin) cout << temp;
        cout << endl;
        int c = a - b;
        displayInfo(c);


    }
    else if (temp == '3') {
        vector<int> multipBin = multiplyBinary(a, b);
        cout << "умножень35е " << a << " и " << b << ": ";
        for (int temp : multipBin) cout << temp;
        cout << endl;
        int c = a * b;
        displayInfo(c);
    }
    else if (temp == '4') {
        vector<string> devidedBin = divideBinary(a, b);
        for (string temp : devidedBin) cout << temp;
        cout << endl;
        float c = static_cast<float>(a) / b;
        displayInfo(c);
    }
    else if (temp == '5') {
        float c;
        float d;
        cout << "введите 2 числа с плавающей точкой ";
        cin >> c >> d;
        vector<bool> BinaryC_2 = BinaryFloat(c);
        cout << "Binary C: ";
        for (auto k : BinaryC_2) {
            cout << k;
        }
        cout << endl;
        vector<bool> BinaryD = BinaryFloat(d);
        cout << "Bibary D: ";
        for (auto k : BinaryD) {
            cout << k;
        }
        cout << endl;
        float res_sum = c + d;
        vector<bool> BinaryRes = BinaryFloat(res_sum);
        cout << "результат сложения чисел " << c << " и " << d << " по стондарту) IEEE-754-2008: ";
        for (auto k : BinaryRes) {
            cout << k;
        }
        cout << endl;
    }
    else return 1;

    goto operations;
    return 0;
}
