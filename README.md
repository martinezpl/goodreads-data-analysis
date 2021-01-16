# Build Week #1

Scrapping/analysis tool for www.goodreads.com. Features:

- CLI providing universal scrapper for goodreads lists.
- Customizable streamlit-based web application hosted on heroku.
- Various analysis functions providing plots and juxtapositions.

#### How to run the scrapper?
Needed packages: click, numpy, pandas, scikit-learn, requests, bs4
1. Download the repo.
2. Set the directory to /bin in the terminal. 
3. Type in *python cli.py scrap-table --help* for further instructions.

**For a quick test:**

*python cli.py scrap-table --pos 10 https://www.goodreads.com/list/show/5.Best_Books_of_the_Decade_2000s*

is going to scrap first 10 positions of the list in given URL and generate scrapped_data.csv in the same folder.


## Team McGonagall

![team](https://github.com/martinezpl/goodreads_best2000/blob/main/pngs/704x396.jpg)

## **Team Players:**

#### Marcin https://github.com/martinezpl

#### Saurabh https://github.com/saurabhsatasia

#### Sai https://github.com/smr-dalli


#### Correlations between parameters:

![correlations](https://github.com/martinezpl/goodreads_best2000/blob/main/pngs/correlations.png)


#### Example visualisation charts:

#### Distribution fit over minmax_norm_rating histogram.
![minmax_dist_fit](https://github.com/martinezpl/goodreads_best2000/blob/main/pngs/2minmax_norm_dist.png)

#### Awards count min_max_norm_rating.
![boxplot_awards](https://github.com/martinezpl/goodreads_best2000/blob/main/pngs/8awards_cnt_minmax_norm_scatter.png)

#### Comparison of minmax & mean normalized ratings.
![normalization comparisons](https://github.com/martinezpl/goodreads_best2000/blob/main/pngs/5comparison_mean_minmax.png)
