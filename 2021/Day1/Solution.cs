using Runner;

namespace Day1;

public class Solution
{
    static private IEnumerable<int> input = Solution.Numbers(Runner.Runner.GetNormalizedInput("Day1/input.in"));

    static void Main(string[] args)
    {
        Console.WriteLine(PartOne);
        Console.WriteLine(PartTwo);
    }

    static int PartOne => Solution.input.Zip(Solution.input.Skip(1), (a, b) => a < b ? 1 : 0).Sum();

    static int PartTwo()
    {
        var input = Solution.input.ToList();

        var total = 0;

        var threeMeasurement1 = 0;
        var threeMeasurement2 = 0;
        for (int i = 0; i + 3 < input.Count; i++)
        {
            threeMeasurement1 = input[i] + input[i + 1] + input[i + 2];
            threeMeasurement2 = input[i + 1] + input[i + 2] + input[i + 3];
            if (threeMeasurement1 < threeMeasurement2)
                total++;
        }

        return total;
    }

    // parse input to array of numbers
    static IEnumerable<int> Numbers(string input) =>
         from n in input.Split('\n')
         select int.Parse(n);
}
