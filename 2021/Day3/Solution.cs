using System.Collections;
using Runner;

namespace Day3;

public class Solution
{
    static private char[][] input = Solution.CharIntTuple(Runner.Runner.GetNormalizedInput("Day3/input.in"));

    static void Main(string[] args)
    {
        Console.WriteLine(PartOne());
    }

    static int PartOne()
    {
        var depth = Solution.input.First().Count();
        var total = Solution.input.Count();

        var oneBits = new int[depth];

        Solution.input.Select(r=> r.Where(b=> b == '1').Count());

        // count ammount of positive bits found
        // Should be optimized, but can't think of a solution atm
        for (int i = 0; i < total; i++)
        {
            for (int j = 0; j < depth; j++)
            {
                if (Solution.input[i][j] == '1')
                    oneBits[j]++;
            }
        }

        var gammaBit = oneBits.Select(c=> c < total/2 ? '1' : '0');
        var gammaInt = Convert.ToInt32(new string(gammaBit.ToArray()), 2);
        var epsilonInt = Convert.ToInt32(new string(gammaBit.Select(g => g == '1' ? '0' : '1').ToArray()), 2);
    
        return gammaInt * epsilonInt;
    }

    // parse input to array of numbers
    static char[][] CharIntTuple(string input) =>
         (from
            line in input.Split('\n')
          let parts = line.Where(c => c != '\r').ToArray()
          select parts).ToArray();
}
