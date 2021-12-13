namespace Runner;

public class Runner
{
    public static string GetNormalizedInput(string file)
    {
        var input = File.ReadAllText(file);
        if (input.EndsWith("\n"))
        {
            input = input.Substring(0, input.Length - 1);
        }
        return input;
    }
}