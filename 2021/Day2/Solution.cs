using Runner;

namespace Day2;

public class Solution
{
    static private IEnumerable<(char, int)> input = Solution.CharIntTuple(Runner.Runner.GetNormalizedInput("Day2/input.in"));

    // static void Main(string[] args)
    // {
    //     Console.WriteLine(PartOne());
    //     Console.WriteLine(PartTwo());
    // }

    static int PartOne()
    {
        (int, int) location = (0, 0);

        foreach (var direction in Solution.input)
        {
            location = movePart1(location, direction);
        }

        return location.Item1 * location.Item2;
    }

    private static (int, int) movePart1((int, int) location, (char, int) direction)
    {
        switch (direction.Item1)
        {
            case 'f':
                location.Item1 += direction.Item2;
                return location;
            case 'd':
                location.Item2 += direction.Item2;
                return location;
            case 'u':
                location.Item2 -= direction.Item2;
                return location;
            default:
                return location;
        }
    }

    static int PartTwo()
    {
        (int, int, int) location = (0, 0, 0);

        foreach (var direction in Solution.input)
        {
            location = movePart2(location, direction);
        }

        return location.Item1 * location.Item2;
    }

    private static (int, int, int) movePart2((int, int, int) location, (char, int) direction)
    {
        switch (direction.Item1)
        {
            case 'f':
                location.Item1 += direction.Item2;
                location.Item2 += location.Item3 * direction.Item2;
                return location;
            case 'd':
                location.Item3 += direction.Item2;
                return location;
            case 'u':
                location.Item3 -= direction.Item2;
                return location;
            default:
                return location;
        }
    }

    // parse input to array of numbers
    static IEnumerable<(char, int)> CharIntTuple(string input) =>
         from
            line in input.Split('\n')
         let parts = line.Split(" ")
         select (parts[0][0], int.Parse(parts[1]));
}
