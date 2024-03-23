#pragma once
#include <iostream>
#include <vector>
#include <math.h>
#include <string>

using namespace std;

vector<int> decimalToBinary(int n);
vector<int> findOnesComplement(int n);
vector<int> findTwosComplement(int n);
void printBinary(std::vector<int>& binary);
vector<int> addAdditional(int a, int b);
vector<int> subtractBinary(int a, int b);
vector<int> multiplyBinary(int a, int b);
vector<string> divideBinary(int a, int b);
vector<int> floatToBinary(float value);
float binaryToFloat(const std::vector<int>& bits);
vector<int> addFloat(const std::vector<int>& a, const std::vector<int>& b);
void displayInfo(int a);
void displayInfo(float f);
string floattoBinary(float f);
vector<bool> BinaryFloat(float value);
