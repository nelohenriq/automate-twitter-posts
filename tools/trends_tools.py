from langchain.tools import tool
from pytrends.request import TrendReq


class TrendsTools:

    @tool("GoogleTrendsTool")
    def trending_searches_on_google(niche: str):
        """A tool to fetch trending Google searches in a given niche for Portugal."""
        try:
            # Initialize the pytrends request
            pytrends = TrendReq(hl="pt-PT", tz=360)

            # Build the payload for the keyword, setting the geographic location to Portugal
            pytrends.build_payload(
                [niche], cat=0, timeframe="today 1-w", geo="PT", gprop=""
            )

            # Get related queries
            related_queries = pytrends.related_queries()

            # Extract and return the top related queries for the given niche
            if niche in related_queries and related_queries[niche]["top"] is not None:
                return related_queries[niche]["top"]
            else:
                return f"No trending searches found for niche: {niche}"

        except Exception as e:
            # Handle exceptions and return an error message
            return f"An error occurred: {str(e)}"
