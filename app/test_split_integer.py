from app import split_integer


class TestSplitInteger:
    def test_sum_of_the_parts_should_be_equal_to_value(self) -> None:
        """Ensure the sum of parts equals the original value."""
        cases = [(3, 3), (17, 4), (9, 3), (2, 4), (100, 9)]
        for value, parts in cases:
            result = split_integer.split_integer(value, parts)
            assert sum(result) == value, f"Sum mismatch for {value} {parts}"

    def test_should_split_into_equal_parts_when_value_divisible_by_parts(
        self,
    ) -> None:
        """Check equal split when value divisible by number of parts."""
        result = split_integer.split_integer(9, 3)
        assert all(
            x == result[0] for x in result
        ), "Not all parts equal for divisible value"

    def test_should_return_part_equals_to_value_when_split_into_one_part(
        self,
    ) -> None:
        """Check single part case."""
        result = split_integer.split_integer(3, 1)
        assert result == [3], f"Expected [3], got {result}"

    def test_parts_should_be_sorted_when_they_are_not_equal(self) -> None:
        """Ensure result is sorted."""
        result = split_integer.split_integer(17, 4)
        assert result == sorted(result), "Result is not sorted"

    def test_should_add_zeros_when_value_is_less_than_number_of_parts(
        self,
    ) -> None:
        """Add zeros when value < parts."""
        result = split_integer.split_integer(2, 4)
        assert sorted(result) == [0, 0, 1, 1], f"[0, 0, 1, 1], got {result}"

    def test_difference_between_parts_should_be_at_most_one(self) -> None:
        """Ensure all parts differ by at most one."""
        cases = [(17, 4), (10, 3), (2, 4), (100, 9), (7, 3)]
        for value, parts in cases:
            result = split_integer.split_integer(value, parts)
            max_diff = max(result) - min(result)
            assert max_diff <= 1, (
                f"Parts differ by more than 1 for {value=} {parts=}"
            )

    def test_should_return_correct_number_of_parts(self) -> None:
        """Ensure correct number of parts returned."""
        cases = [(17, 4), (2, 4), (9, 3), (1, 5)]
        for value, parts in cases:
            result = split_integer.split_integer(value, parts)
            assert len(result) == parts, (
                f"Expected {parts} parts, got {len(result)}"
            )

    def test_result_should_not_depend_on_order_of_distribution(self) -> None:
        """Remainder distribution should not affect sorted result."""
        cases = [(10, 3), (11, 4), (17, 4), (2, 4)]
        for value, parts in cases:
            result = split_integer.split_integer(value, parts)
            expected = sorted(result)
            assert result == expected, "Result order inconsistency"
