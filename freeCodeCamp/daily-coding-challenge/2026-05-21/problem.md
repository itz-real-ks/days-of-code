# I Before E
### Problem statement: Given a word or sentence, return a corrected version where every word follows the "I before E except after C" rule.

- If a word contains "ei" not preceded by "c", replace it with "ie".
- If a word contains "ie" preceded by "c", replace it with "ei".
- All other words are left unchanged.

>Tests:

Waiting:1. `i_before_e("beleive") should return "believe".`

Waiting:2. `i_before_e("recieve") should return "receive".`

Waiting:3. `i_before_e("we recieved a breif") should return "we received a brief".`

Waiting:4. `i_before_e("she beleived the friendly niece could percieve the greif") should return "she believed the friendly niece could perceive the grief".`

Waiting:5. `i_before_e("we recieved relief after the theif gave us a breif piece of feirce deceit") should return "we received relief after the thief gave us a brief piece of fierce deceit".`