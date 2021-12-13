using Runner;

namespace Day2;

public class Solution
{
    static private IEnumerable<(string, int)> input = Solution.StringIntTuple(Runner.Runner.GetNormalizedInput("Day1/input.in"));

    static void Main(string[] args)
    {
        Console.WriteLine(PartOne());
        // Console.WriteLine(PartTwo);
    }

    static int PartOne()
    {
        (int, int) location = (0,0);

        foreach (var direction in Solution.input)
        {
            location = move(location, direction);
        }

        return location.Item1 * location.Item2;
    }

    private static (int, int) move((int, int) location, (char, int) direction)
    {
        switch (direction.Item1)
        {
            case 'f':
                location.Item1 += direction.Item2;
                return location;
            case 'd':
                location.Item2 -= direction.Item2;
                return location;
            case 'u':
                location.Item2 += direction.Item2;
                return location;
            default:
                return location;
        }
    }


    //     static int PartTwo()
    //     {
    //         var input = Solution.input.ToList();
    //
    //         var total = 0;
    //
    //         var threeMeasurement1 = 0;
    //         var threeMeasurement2 = 0;
    //         for (int i = 0; i + 3 < input.Count; i++)
    //         {
    //             threeMeasurement1 = input[i] + input[i + 1] + input[i + 2];
    //             threeMeasurement2 = input[i + 1] + input[i + 2] + input[i + 3];
    //             if (threeMeasurement1 < threeMeasurement2)
    //                 total++;
    //         }
    //
    //         return total;
    //     }

    // parse input to array of numbers
    static IEnumerable<(char, int)> StringIntTuple(string input) =>
         from 
            line in input.Split('\n')
            let parts = line.Split()
        select (parts[0], int.Parse(parts[1]));
}
