#include "gtest/gtest.h"
#include "pch.h"
#include "../LibLW1/Source.cpp" // ���������� ��� ������ ����� � �����

// ����� ��� ������� decimalToBinary
TEST(DecimalToBinaryTest, PositiveNumber) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 0, 0, 1 }; 
    EXPECT_EQ(decimalToBinary(9), expected);
}

TEST(DecimalToBinaryTest, NegativeNumber) {
    std::vector<int> expected = { 1, 0, 0, 0, 1, 0, 0, 1 }; 
    EXPECT_EQ(decimalToBinary(-9), expected);
}

// ����� ��� ������� findOnesComplement
TEST(FindOnesComplementTest, PositiveNumber) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 0, 0, 1 }; 
    EXPECT_EQ(findOnesComplement(9), expected);
}

TEST(FindOnesComplementTest, NegativeNumber) {
    std::vector<int> expected = { 1, 1, 1, 1, 0, 1, 1, 0 }; 
    EXPECT_EQ(findOnesComplement(-9), expected);
}

// ����� ��� ������� findTwosComplement
TEST(FindTwosComplementTest, PositiveNumber) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 0, 0, 1 }; 
    EXPECT_EQ(findTwosComplement(9), expected);
}

TEST(FindTwosComplementTest, NegativeNumber) {
    std::vector<int> expected = { 1, 1, 1, 1, 0, 1, 1, 1 }; 
    EXPECT_EQ(findTwosComplement(-9), expected);
}

// ����� ��� ������� addAdditional
TEST(AddAdditionalTest, BasicTest) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 0, 0, 0 };
    EXPECT_EQ(addAdditional(5, 3), expected);
}

// ����� ��� ������� subtractBinary
TEST(SubtractBinaryTest, BasicTest) {
    std::vector<int> expected = { 0, 0, 0, 0, 0, 0, 1, 0 };
    EXPECT_EQ(subtractBinary(5, 3), expected);
}

// ����� ��� ������� multiplyBinary
TEST(MultiplyBinaryTest, BasicTest) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 1, 1, 1 };
    EXPECT_EQ(multiplyBinary(5, 3), expected);
}

// ����� ��� ������� divideBinary


// ����� ��� ������� floatToBinary
TEST(FloatToBinaryTest, PositiveNumber) {
    std::vector<int> expected = { 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    EXPECT_EQ(floatToBinary(12.5f), expected);
}

TEST(FloatToBinaryTest, Zero) {
    std::vector<int> expected(32, 0);
    EXPECT_EQ(floatToBinary(0.0f), expected);
}

// ����� ��� ������� addFloat
TEST(AddFloatTest, BasicTest) {
    std::vector<int> binaryA = { 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    std::vector<int> binaryB = { 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    std::vector<int> expected = { 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    EXPECT_EQ(addFloat(binaryA, binaryB), expected);
}

int main(int argc, char** argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
