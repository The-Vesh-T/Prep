# Notes and Things Learned

## Initial backtester creation 4 / 19 / 2026
- While based off data we can assume a Fair value, if something major happens this can change resulting in the algorithm to fully break. We should therefore use rolling averages which require looking at a set amount of data from the whole. This can be achieved using window!
- Pandas always useful for csv and data
- variable:,.2f adds commas and .2f is for 2 decimal places!
- Position is how much of the asset you're holding, impose a limit depending on rules.
So far we're using just position between 0 and 1 to test how it works and stress testing. When i switched it to buy high sell low we ended negative which is good since the code works LOL. Overall it depends on the window which makes sense. The bigger the window the more accurate the avg is but if its smaller it could mess up. However if something major happens a bigger window size could cause issues. Its about finding the right balance.
- hyperparameter tuning and bias-variance tradeoff

### Questions
So far I set up basic buy low sell high logic by using position between 0 and 1 and rolling averages. However I honestly see so many issues and areas to expand, not really issues since this is v1, but just ways to expand in almost every direction.
- How would buying more work? does that mean we buy/sell only 1 per tick especially if we put a limit like 80?
- If we have too much inventory then should we auto sell? position>50??? But then we could lose money...
- In future when we buy more quantity we might run into a full inventory before the price is at its lowest. How would we track and know this? Theoretically if we track the trend ex 10 to 9 to 8 to 7 to 8. We would track and see we hit 7 meaning we hit the lowest but by time we buy we're no longer at 7 we're a tick ahead at 8. How would we deal with this 'lag'?
- Momentum?