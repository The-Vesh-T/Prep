# Notes and Things Learned

### 4 / 19 / 2026
- While based off data we can assume a Fair value, if something major happens this can change resulting in the algorithm to fully break. We should therefore use rolling averages which require looking at a set amount of data from the whole. This can be achieved using window!
- Pandas always useful for csv and data
- variable:,.2f adds commas and .2f is for 2 decimal places!
- Position is how much of the asset you're holding, impose a limit depending on rules.
So far we're using just position between 0 and 1 to test how it works and stress testing. When i switched it to buy high sell low we ended negative which is good since the code works LOL. Overall it depends on the window which makes sense. The bigger the window the more accurate the avg is but if its smaller it could mess up. However if something major happens a bigger window size could cause issues. Its about finding the right balance.
- hyperparameter tuning and bias-variance tradeoff