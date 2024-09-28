import re

class ConversationalModel:
    def __init__(self):
        self.responses = {
            "length": "len(data)",
            "rows": "len(data)",
            "columns": "len(data.columns)",
            "summary": "data.describe()",
            "column": "data.columns",
            "head": "data.head()",
            "tail": "data.tail()",
            "unique": "data.nunique()",
            "info": "data.info()",
            "missing": "data.isnull().sum()",
            "value_counts": "data['column_name'].value_counts()",
            "mean": "data.mean()",
            "median": "data.median()",
            "mode": "data.mode()",
            "min": "data.min()",
            "max": "data.max()",
            "std": "data.std()",
            "var": "data.var()",
            "corr": "data.corr()",
            "groupby": "data.groupby('column_name').mean()",
            "plot": "data['column_name'].plot(kind='hist')",
            "scatter": "data.plot(kind='scatter', x='column_name1', y='column_name2')",
            "boxplot": "data.boxplot(column='column_name')",
            "heatmap": "sns.heatmap(data.corr(), annot=True)",
            "pairplot": "sns.pairplot(data)",
            "countplot": "sns.countplot(data['column_name'])",
            "barplot": "sns.barplot(x='column_name1', y='column_name2', data=data)",
            "lineplot": "sns.lineplot(x='column_name1', y='column_name2', data=data)",
            "piechart": "data['column_name'].value_counts().plot(kind='pie')",
            "histogram": "data['column_name'].plot(kind='hist')",
            "describe": "data.describe()",
            "sample": "data.sample()",
            "drop": "data.drop(['column_name'], axis=1)",
            "dropna": "data.dropna()",
            "fillna": "data.fillna(value)",
            "replace": "data.replace(to_replace, value)",
            "sort_values": "data.sort_values('column_name')",
            "reset_index": "data.reset_index()",
            "set_index": "data.set_index('column_name')",
            "merge": "pd.merge(data1, data2, on='column_name')",
            "concat": "pd.concat([data1, data2], axis=1)",
            "join": "data1.join(data2, on='column_name')",
            "pivot_table": "pd.pivot_table(data, values='column_name1', index='column_name2', columns='column_name3', aggfunc='mean')",
            "groupby": "data.groupby('column_name').mean()",
            "apply": "data['column_name'].apply(function)",
            "applymap": "data.applymap(function)",
            "lambda": "lambda x: x**2",
            "loc": "data.loc['row_name']",
            "iloc": "data.iloc[0]",
        }

        self.synonyms = {
            "length": ["lenght of the dataset", "total length of the dataset", "len", "what is the len of the dataset", "what is the lenght of this dataset"],
            "rows": ["number of rows", "total number of rows", "row count", "how many rows are there", "how many rows"],
            "column": ["number of columns", "total number of columns", "column count", "how many columns are there", "how many columns"],
            "summary": ["summary of the dataset", "describe the dataset", "data.describe()", "describe", "summary of the data"],
            "columns": ["show columns", "display columns", "what are the columns", "what are the column names", "column names"],
            "head": ["show head", "display head", "what is the head", "what is the head of the dataset", "head of the dataset"],
            "tail": ["show tail", "display tail", "what is the tail", "what is the tail of the dataset", "tail of the dataset"],
            "unique": ["unique values", "unique entries", "unique elements", "unique items", "unique count"],
            "info": ["information", "data information", "data info", "data.info()", "info of the dataset"],
            "missing": ["missing values", "null values", "empty values", "missing data", "missing entries"],
            "value_counts": ["value counts", "count of values", "frequency of values", "value frequency", "value distribution"],
            "mean": ["average", "mean value", "mean calculation", "mean of the data", "mean of the dataset"],
            "median": ["middle value", "median value", "median calculation", "median of the data", "median of the dataset"],
            "mode": ["most common value", "mode value", "mode calculation", "mode of the data", "mode of the dataset"],
            "min": ["minimum value", "smallest value", "minimum calculation", "minimum of the data", "minimum of the dataset"],
            "max": ["maximum value", "largest value", "maximum calculation", "maximum of the data", "maximum of the dataset"],
            "std": ["standard deviation", "std value", "std calculation", "std of the data", "std of the dataset"],
            "var": ["variance", "variance value", "variance calculation", "variance of the data", "variance of the dataset"],
            "corr": ["correlation", "correlation value", "correlation calculation", "correlation of the data", "correlation of the dataset"],
            "groupby": ["group by", "grouping", "group by column", "group by operation", "group by the column"],
            "plot": ["plotting", "plot the data", "plot the column", "plot the values", "plot the distribution"],
            "scatter": ["scatter plot", "scatter diagram", "scatter graph", "scatter visualization", "scatter plot of the data"],
            "boxplot": ["box plot", "box diagram", "box graph", "box visualization", "box plot of the data"],
            "heatmap": ["heat map", "heat diagram", "heat graph", "heat visualization", "heat map of the data"],
            "pairplot": ["pair plot", "pair diagram", "pair graph", "pair visualization", "pair plot of the data"],
            "countplot": ["count plot", "count diagram", "count graph", "count visualization", "count plot of the data"],
            "barplot": ["bar plot", "bar diagram", "bar graph", "bar visualization", "bar plot of the data"],
            "lineplot": ["line plot", "line diagram", "line graph", "line visualization", "line plot of the data"],
            "piechart": ["pie chart", "pie diagram", "pie graph", "pie visualization", "pie chart of the data"],
            "histogram": ["histogram plot", "histogram diagram", "histogram graph", "histogram visualization", "histogram of the data"],
            "describe": ["describe the data", "describe the dataset", "describe the values", "describe the distribution", "describe the summary"],
            "sample": ["random sample", "random data", "random values", "random entries", "random selection"],
            "drop": ["drop column", "remove column", "delete column", "drop the column", "remove the column"],
            "dropna": ["drop missing values", "remove null values", "delete empty values", "drop the missing values", "remove the missing values"],
            "fillna": ["fill missing values", "replace null values", "complete empty values", "fill the missing values", "replace the missing values"],
            "replace": ["replace values", "substitute values", "change values", "replace the values", "substitute the values"],
            "sort_values": ["sort the data", "sort the dataset", "sort the values", "sort the entries", "sort the distribution"],
            "reset_index": ["reset the index", "reset the dataset", "reset the values", "reset the entries", "reset the distribution"],
            "set_index": ["set the index", "set the dataset", "set the values", "set the entries", "set the distribution"],
            "merge": ["merge data", "combine data", "join data", "merge the data", "combine the data"],
            "concat": ["concatenate data", "combine data", "join data", "concatenate the data", "combine the data"],
            "join": ["join data", "combine data", "merge data", "join the data", "combine the data"],
            "pivot_table": ["pivot table", "pivot data", "pivot operation", "pivot the data", "pivot the values"],
            "groupby": ["group by", "grouping", "group by column", "group by operation", "group by the column"],
            "apply": ["apply function", "use function", "apply operation", "apply the function", "use the function"],
            "applymap": ["apply function", "use function", "apply operation", "apply the function", "use the function"],
            "lambda": ["lambda function", "anonymous function", "lambda operation", "lambda expression", "lambda calculation"],
            "loc": ["locate row", "locate entry", "locate value", "locate the row", "locate the entry"],
            "iloc": ["integer locate", "integer entry", "integer value", "integer locate the row", "integer locate the entry"],
        }

        self.context = {}

    def get_response(self, input):
        input = self.normalize(input)
        response = self.pattern_matching(input)
        return response or "I don't understand that."

    def normalize(self, input):
        input = input.lower()
        input = re.sub(r'[^\w\s]', '', input)
        return input

    def pattern_matching(self, input):
        for pattern in self.responses:
            if re.search(rf'\b{pattern}\b', input):
                return self.responses[pattern]

        for synonym, words in self.synonyms.items():
            for word in words:
                if re.search(rf'\b{word}\b', input):
                    return self.responses[synonym]
        return None

    def named_entity_recognition(self, input):
        match = re.search(r'\bmy name is (\w+)\b', input)
        if match:
            name = match.group(1)
            self.context["name"] = name
            return f"Nice to meet you, {name}!"
        return None

    def sentiment_analysis(self, input):
        if re.search(r'\b(happy|great|good)\b', input):
            return "I'm glad to hear that!"
        elif re.search(r'\b(sad|bad|terrible)\b', input):
            return "I'm sorry to hear that. I hope things get better soon."
        return None

    def dynamic_response_generation(self, input):
        if "name" in self.context:
            return f"How can I assist you today, {self.context['name']}?"
        return None

