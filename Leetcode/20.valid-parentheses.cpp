/*
 * @lc app=leetcode id=20 lang=cpp
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution
{
public:
    bool isValid(string s)
    {
        stack<char> S;
        for (auto c : s)
        {
            if (c == '(' || c == '{' || c == '[')
            {
                S.push(c);
            }
            else
            {
                if (S.empty())
                {
                    return false;
                }
                char top = S.top();
                if ((c == ')' && top == '(') || (c == '}' && top == '{') || (c == ']' && top == '['))
                {
                    S.pop();
                }
                else
                {
                    return false;
                }
            }
        }
        return S.empty();
    }
};
// @lc code=end
