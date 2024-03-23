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
    cout << "��������� �������� ������� ������2� �����������:\n 1. �������� ����� � ���������������� ����.\n 2. ��������1� � ������������� ����\n 3. ��������) ����� � �������������� ����\n 4. ������� ����� � ������ ����\n 5. ����������� ����� �� ��������� IEEE-754-2008\n ";
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
        cout << "���������4� " << a << " � " << b << ": ";
        for (int temp : substractedBin) cout << temp;
        cout << endl;
        int c = a - b;
        displayInfo(c);


    }
    else if (temp == '3') {
        vector<int> multipBin = multiplyBinary(a, b);
        cout << "��������35� " << a << " � " << b << ": ";
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
        cout << "������� 2 ����� � ��������� ������ ";
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
        cout << "��������� �������� ����� " << c << " � " << d << " �� ���������) IEEE-754-2008: ";
        for (auto k : BinaryRes) {
            cout << k;
        }
        cout << endl;
    }
    else return 1;

    goto operations;
    return 0;
}
