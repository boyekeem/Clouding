import networkx
import twitter
g=networkx.Graph()
g.add_edge(1,2)
g.add_node("spam")
print g.nodes()
print g.edges()

twitter_search=twitter.Twitter(domain= "search.twitter.com")
trends=twitter_search.trends()
[ trend["name"] for trend in trends["trends"] ]