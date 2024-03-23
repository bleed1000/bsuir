#include "gtest/gtest.h"
#include "pch.h"
#include "../LibLW1/Source.cpp" // Подставьте имя вашего файла с кодом

// Тесты для функции decimalToBinary
TEST(DecimalToBinaryTest, PositiveNumber) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 0, 0, 1 }; 
    EXPECT_EQ(decimalToBinary(9), expected);
}

TEST(DecimalToBinaryTest, NegativeNumber) {
    std::vector<int> expected = { 1, 0, 0, 0, 1, 0, 0, 1 }; 
    EXPECT_EQ(decimalToBinary(-9), expected);
}

// Тесты для функции findOnesComplement
TEST(FindOnesComplementTest, PositiveNumber) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 0, 0, 1 }; 
    EXPECT_EQ(findOnesComplement(9), expected);
}

TEST(FindOnesComplementTest, NegativeNumber) {
    std::vector<int> expected = { 1, 1, 1, 1, 0, 1, 1, 0 }; 
    EXPECT_EQ(findOnesComplement(-9), expected);
}

// Тесты для функции findTwosComplement
TEST(FindTwosComplementTest, PositiveNumber) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 0, 0, 1 }; 
    EXPECT_EQ(findTwosComplement(9), expected);
}

TEST(FindTwosComplementTest, NegativeNumber) {
    std::vector<int> expected = { 1, 1, 1, 1, 0, 1, 1, 1 }; 
    EXPECT_EQ(findTwosComplement(-9), expected);
}

// Тесты для функции addAdditional
TEST(AddAdditionalTest, BasicTest) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 0, 0, 0 };
    EXPECT_EQ(addAdditional(5, 3), expected);
}

// Тесты для функции subtractBinary
TEST(SubtractBinaryTest, BasicTest) {
    std::vector<int> expected = { 0, 0, 0, 0, 0, 0, 1, 0 };
    EXPECT_EQ(subtractBinary(5, 3), expected);
}

// Тесты для функции multiplyBinary
TEST(MultiplyBinaryTest, BasicTest) {
    std::vector<int> expected = { 0, 0, 0, 0, 1, 1, 1, 1 };
    EXPECT_EQ(multiplyBinary(5, 3), expected);
}

// Тесты для функции divideBinary


// Тесты для функции floatToBinary
TEST(FloatToBinaryTest, PositiveNumber) {
    std::vector<int> expected = { 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 };
    EXPECT_EQ(floatToBinary(12.5f), expected);
}

TEST(FloatToBinaryTest, Zero) {
    std::vector<int> expected(32, 0);
    EXPECT_EQ(floatToBinary(0.0f), expected);
}

// Тесты для функции addFloat
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
