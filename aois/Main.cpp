#include "..\LibLW1\Header.h"

int main() {
    setlocale(LC_ALL, "rus");
    cout << "������� ������ ����� � ���������� �������\n";
    int a;
    cin >> a;
    displayInfo(a);
    cout << "������� ������ ������ � ���������� �������\n";
    int b;
    cin >> b;
    displayInfo(b);

operations:
    cout << "�������� �������� ������� ������ ��������:\n 1. ��������� ������ � �������������� ����.\n 2. ��������� � ������������� ����\n 3. ������� ����� � �������������� ����\n 4. ������� ������ � ������ ����\n 5. ��������� ������ �� ��������� IEEE-754-2008\n ";
    char temp;
    cin >> temp;
    if (temp == '1') {
        vector<int> ans = addAdditional(a, b);
        cout << "�������� " << a << " � " << b << ": ";
        for (int temp : ans) cout << temp;
        cout << endl;
        int c = a + b;
        displayInfo(c);
    }
    else if (temp == '2') {
        vector<int> substractedBin = subtractBinary(a, b);
        cout << "��������� " << a << " � " << b << ": ";
        for (int temp : substractedBin) cout << temp;
        cout << endl;
        int c = a - b;
        displayInfo(c);


    }
    else if (temp == '3') {
        vector<int> multipBin = multiplyBinary(a, b);
        cout << "��������� " << a << " � " << b << ": ";
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
        cout << "������� 2 ����� � ��������� ������ ";
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
        cout << "��������� �������� ������ " << c << " � " << d << " �� ��������� IEEE-754-2008: ";
        for (int temp : result) {
            cout << temp;
        }
        cout << endl;
    }
    else return 1;

    goto operations;
    return 0;
}
