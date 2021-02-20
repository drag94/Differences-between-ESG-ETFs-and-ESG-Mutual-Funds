# Grafici etf-Mutual funds (prossimo rete neur convoluzionale)

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

if __name__ == '__main__':

    path_etf = "/home/davide/PycharmProjects/pythonProject2/mornstar scripts/Morningstar - European ETFs.csv"
    path_mutualfund = "/home/davide/PycharmProjects/pythonProject2/mornstar scripts/Morningstar - European Mutual Funds.csv"

    cols_name = [
        'inception_date',
        'isin',
        'category',
        'morningstar_benchmark',
        'dividend_frequency',

        'performance_rating',
        'nav_per_share_currency',
        'nav_per_share',
        'performance_rating',

        'fund_trailing_return_ytd',  'fund_trailing_return_3years',
        'fund_trailing_return_5years',
        'equity_style',
        'equity_size',
        # 'price_prospective_earnings','price_book_ratio', 'price_sales_ratio','price_cash_flow_ratio','dividend_yield_factor', #value factors
        # 'long_term_projected_earnings_growth', 'historical_earnings_growth','sales_growth', 'cash_flow_growth','book_value_growth', #growth factors
        # 'asset_stock',
        # 'asset_bond',
        # 'asset_cash',
        # 'asset_other',
        # 'holdings_n_stock',
        # 'holdings_n_bonds',
         'sustainability_rank', 'environmental_score', 'social_score', 'governance_score', 'sustainability_score']


    df_etf = pd.read_csv(path_etf,
                         usecols=cols_name,index_col='isin')
    df_mfund = pd.read_csv(path_mutualfund,
                           usecols=cols_name,index_col='isin')
    #Converting time in datetime objects
    df_etf['inception_date'] = pd.to_datetime(df_etf.inception_date)
    df_mfund['inception_date'] = pd.to_datetime(df_mfund.inception_date)

    numeric_var_etf = [key for key in dict(df_etf.dtypes)
                       if dict(df_etf.dtypes)[key]
                       in ['float64', 'float32', 'int32', 'int64']]  # Numeric Variable

    cat_var_etf = [key for key in dict(df_etf.dtypes)
                   if dict(df_etf.dtypes)[key] in ['object']]  # dtype O mixed values

    print('Columns with numeric values (train set): ' + str(numeric_var_etf.__len__()),
          '\n#Columns with non-numeric values (train set): ' + str(cat_var_etf.__len__()) +
          '\nwhich features: '+str(cat_var_etf))


    numeric_var_mfund = [key for key in dict(df_mfund.dtypes)
                         if dict(df_mfund.dtypes)[key]
                         in ['float64', 'float32', 'int32', 'int64']]  # Numeric Variable

    cat_var_mfund = [key for key in dict(df_mfund.dtypes)
                     if dict(df_mfund.dtypes)[key] in ['object']]  # dtype O mixed values

    print('# Columns with numeric values (test set): ' + str(numeric_var_mfund.__len__())
          ,'\n# Columns with non-numeric values (test set): ' + str(cat_var_mfund.__len__()) +
          '\nwhich features: ' + str(cat_var_mfund))
    #
    # Executive Summary
    # Funds with higher star ratings (4- and 5-star) outperformed their average peers during the recent sell-off and the rally that preceded it, while lower-rated funds (1- and 2-star) underperformed. Over the full period spanning the rally and sell-off, 5-star funds topped their average peer by about 1.25% per year while 1-star funds lagged by roughly 2% per year. All told, higher-rated funds were about 1.5 times more likely to beat their category average than lower-rated funds over the full period.

    df_etf_num = df_etf[numeric_var_etf]
    df_mfund_num = df_mfund[numeric_var_mfund]

    sns.set(style='darkgrid')

    fig, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1,figsize=(30,30),sharex=True,sharey=True)
    sns.histplot(data=df_etf_num[(df_etf_num['fund_trailing_return_ytd']>=-20) & (df_etf_num['fund_trailing_return_ytd']<=30)]['fund_trailing_return_ytd'],kde=True,ax=ax1)
    sns.histplot(data=df_etf_num[(df_etf_num['fund_trailing_return_3years']>=-20) & (df_etf_num['fund_trailing_return_3years']<=30)]['fund_trailing_return_3years'],kde=True,ax=ax2)
    sns.histplot(data=df_etf_num[(df_etf_num['fund_trailing_return_5years']>=-20) & (df_etf_num['fund_trailing_return_5years']<=30)]['fund_trailing_return_5years'],kde=True,ax=ax3)
    ax1.set_title('ETFs YearToDate return (%)')
    ax2.set_title('ETFs -3years return (%)')
    ax3.set_title('ETFs -5years return (%)')
    ax3.set_xlabel('Return')
    ax1m=np.mean(df_etf_num[(df_etf_num['fund_trailing_return_ytd']>=-20) & (df_etf_num['fund_trailing_return_ytd']<=30)]['fund_trailing_return_ytd'])
    ax2m=np.mean(df_etf_num[(df_etf_num['fund_trailing_return_3years']>=-20) & (df_etf_num['fund_trailing_return_3years']<=30)]['fund_trailing_return_3years'])
    ax3m=np.mean(df_etf_num[(df_etf_num['fund_trailing_return_5years']>=-20) & (df_etf_num['fund_trailing_return_5years']<=30)]['fund_trailing_return_5years'])
    ax1.axvline(x=ax1m,ls='--',c='b',linewidth=3, label='mean at {}'.format(round(ax1m,2)))
    ax1.axvline(x=0,ls='--',c='green',linewidth=3)
    ax2.axvline(x=ax2m,ls='--',c='b',linewidth=3, label='mean at {}'.format(round(ax2m,2)))
    ax2.axvline(x=0,ls='--',c='green',linewidth=3)
    ax3.axvline(x=ax3m,ls='--',c='b',linewidth=3,label='mean at {}'.format(round(ax3m,2)))
    ax3.axvline(x=0,ls='--',c='green',linewidth=3)
    ax1.legend()
    ax2.legend()
    ax3.legend()
    plt.show()
    fig.set_tight_layout(True)

    fig2, (ax1,ax2,ax3) = plt.subplots(nrows=3,ncols=1,figsize=(30,30),sharex=True,sharey=True)
    sns.histplot(data=df_mfund_num[(df_mfund_num['fund_trailing_return_ytd']>=-20) & (df_mfund_num['fund_trailing_return_ytd']<=30)]['fund_trailing_return_ytd'],kde=True,ax=ax1)
    sns.histplot(data=df_mfund_num[(df_mfund_num['fund_trailing_return_3years']>=-20) & (df_mfund_num['fund_trailing_return_3years']<=30)]['fund_trailing_return_3years'],kde=True,ax=ax2)
    sns.histplot(data=df_mfund_num[(df_mfund_num['fund_trailing_return_5years']>=-20) & (df_mfund_num['fund_trailing_return_5years']<=30)]['fund_trailing_return_5years'],kde=True,ax=ax3)
    ax1.set_title('Mutual Funds YearToDate return (%)')
    ax2.set_title('Mutual Funds -trailing 3years return (%)')
    ax3.set_title('Mutual Funds -trailing 5years return (%)')
    ax3.set_xlabel('Return')
    ax1m_mf=np.mean(df_mfund_num[(df_mfund_num['fund_trailing_return_ytd']>=-20) & (df_mfund_num['fund_trailing_return_ytd']<=30)]['fund_trailing_return_ytd'])
    ax2m_mf=np.mean(df_mfund_num[(df_mfund_num['fund_trailing_return_3years']>=-20) & (df_mfund_num['fund_trailing_return_3years']<=30)]['fund_trailing_return_3years'])
    ax3m_mf=np.mean(df_mfund_num[(df_mfund_num['fund_trailing_return_5years']>=-20) & (df_mfund_num['fund_trailing_return_5years']<=30)]['fund_trailing_return_5years'])
    ax1.axvline(x=ax1m_mf,ls='--',c='b',linewidth=3, label='mean at {}'.format(round(ax1m_mf,2)))
    ax1.axvline(x=0,ls='--',c='green',linewidth=3)
    ax2.axvline(x=ax2m_mf,ls='--',c='b',linewidth=3,label='mean at {}'.format(round(ax2m_mf,2)))
    ax2.axvline(x=0,ls='--',c='green',linewidth=3)
    ax3.axvline(x=ax3m_mf,ls='--',c='b',linewidth=3,label='mean at {}'.format(round(ax3m_mf,2)))
    ax3.axvline(x=0,ls='--',c='green',linewidth=3)
    ax1.legend()
    ax2.legend()
    ax3.legend()
    plt.show()
    fig2.set_tight_layout(True)

    df_mfund_category = df_mfund['category'].dropna()
    df_mfund_cat10 = df_mfund_category.value_counts()[:10]

    plt.figure(figsize=(15, 15),dpi=200)
    sns.barplot(df_mfund_cat10.values, df_mfund_cat10.index,
                color='deepskyblue',edgecolor=".9")
    #for i, v in enumerate(df_mfund_cat10.values):
    #    plt.text(0.8,i,v,color='k',fontsize=12)

    plt.title("Mutual Funds - categories", fontsize=13)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.show()

    df_etf_category = df_etf['category'].dropna()

    plt.figure(figsize=(15, 15),dpi=200)
    df_etf_cat10 = df_etf_category.value_counts()[:10]
    sns.barplot(df_etf_cat10.values, df_etf_cat10.index,
                color='blue',edgecolor=".9")
    #for a, b in enumerate(df_etf_cat10.values):
    #    plt.text(0.8,a,b,color='k',fontsize=12)

    plt.title("ETFs - categories",fontsize=13)
    plt.xticks(fontsize=8)
    plt.yticks(fontsize=8)
    plt.tight_layout()
    plt.show()

    # Number of benchamrks in either etfs and mf
    print(' n ETF benchmarks =' + str(df_etf.morningstar_benchmark.nunique()),
          ' n Mutualfunds benchmarks ='+str(df_mfund.morningstar_benchmark.nunique()))
    df_etf_bench = df_etf['morningstar_benchmark'].dropna().value_counts()[:10]
    df_mfund_bench = df_mfund['morningstar_benchmark'].dropna().value_counts()[:10]

    plt.figure(figsize=(15,15),dpi=150)
    sns.barplot(df_etf_bench.values,df_etf_bench.index,
                color= 'blue', #palette="rocket",
                edgecolor=".9")
    plt.title('ETFs - The most common benchmarks')
    #for c, d in enumerate(df_etf_bench.values):
    #    plt.text(0.5,c,d,color='black',fontsize=9)
    plt.tick_params(labelsize=8,direction='out')
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(15,15),dpi=150)
    sns.barplot(df_mfund_bench.values,df_mfund_bench.index,

             color='deepskyblue',#palette="rocket",
                edgecolor=".9")
    plt.title('Mutual Funds - The most common benchmarks')
    #for e, f in enumerate(df_mfund_bench.values):
    #    plt.text(0.5,e,f,color='black',fontsize=9)
    plt.tick_params(labelsize=8,direction='out')
    plt.tight_layout()
    plt.show()

    df_etf_eqst = df_etf['equity_style'].dropna().value_counts()
    df_mfund_eqst = df_mfund['equity_style'].dropna().value_counts()
    df_eqst = pd.DataFrame({'equity_style_ETF':df_etf_eqst.values,'equity_style_MutualFunds':df_mfund_eqst.values},index=['Blend','Value','Growth'])

    fig5, (ax4,ax5) = plt.subplots(1,2,figsize=(15,15))
    recipe = df_eqst.index
    data = df_eqst.values
    ingredients = df_eqst.index
    def func(pct, allvals):
        absolute = int(pct/100.*np.sum(allvals))
        return "{:.1f}%\n({:d})".format(pct, absolute)
    wedgesetf, textsetf, autotextsetf = ax4.pie(data[:,0], autopct=lambda pct: func(pct, data[:,0]),
                                                textprops=dict(color="w"),
                                                explode=(0.05,0,0))
    wedgesmf, textsmf, autotextsmf = ax5.pie(data[:,1], autopct=lambda pct: func(pct, data[:,1]),
                                             textprops=dict(color="w"),
                                             explode=(0.05,0,0))
    ax4.legend(wedgesetf, ingredients,
               title="ETFs - Equity style",
               loc="center", fontsize='medium',
               bbox_to_anchor=(.8, .5, .5, 0))
    ax5.legend(wedgesmf, ingredients,
               title="Mutual Funds - Equity style",
               loc="center", fontsize='medium',
               bbox_to_anchor=(.85, .5, .5, 0))
    plt.setp([autotextsetf,autotextsmf], size=15, weight="bold")
    ax4.set_title("ETFs - Equity style", fontdict={'fontsize': 15, 'fontweight': 'medium'})
    ax5.set_title('Mutual Funds - Equity style', fontdict={'fontsize': 15, 'fontweight': 'medium'})
    fig5.set_tight_layout(True)
    plt.show()


    """df_etf_cat10 / df_mfund_cat10"""
    ### ESG ###
    df_mfund_cat = df_mfund.loc[df_mfund['category'].isin(df_mfund_cat10.index)]
    #Since EUR GOV bond's esg score is nan everyhere, i drop the rows in the column category where there is EUR Government Bond from the category list
    df_etf_cat_eurgov = df_etf.loc[df_etf['category'].isin(df_etf_cat10.index)]
    df_etf_cat = df_etf_cat_eurgov.drop(df_etf_cat_eurgov['category'].loc[df_etf_cat_eurgov['category'] == 'EUR Government Bond'].index)
    df_mfund_cat['ESG score'] = df_mfund_cat['sustainability_score']
    df_etf_cat['ESG score'] = df_etf_cat['sustainability_score']

    fig6, ax6 = plt.subplots(1,1,figsize=(15,15),dpi=150)
    sns.boxplot(y=df_mfund_cat['category'],x=df_mfund_cat['ESG score'],
                  palette='muted',orient='h'
                      #k_depth='proportion'
                 )
    #ax6.set_ylabel(ylabel='ESG score', fontsize=8)
    ax6.set_title(label='Mutual Funds (the ones among the most common categories) - ESG score', fontsize=12)
    #plt.xticks(rotation=30,fontsize='small',horizontalalignment='center')
    plt.tick_params(labelsize=8, direction='out')
    plt.xlim(0,40)
    plt.ylabel('')
    fig6.set_tight_layout(True)
    plt.show()

    fig13,ax13 = plt.subplots(1,1,figsize=(15,15),dpi=150)
    sns.boxplot(y=df_etf_cat['category'],x=df_etf_cat['ESG score']
                   ,palette='muted',orient='h')
    #ax13.set_ylabel(ylabel='ESG score', fontsize=10)
    ax13.set_title(label='ETFs (the ones among the most common categories) - ESG score', fontsize=12)
    #plt.xticks(rotation=45,fontsize=10)
    plt.tick_params(labelsize=8, direction='out')
    plt.ylabel('')
    fig13.set_tight_layout(True)
    plt.show()

    ### ENVIRONMENTAL SCORE ###
    fig7,ax7 = plt.subplots(1,1,figsize=(15,15))
    sns.barplot(x=df_etf_cat['category'],y=df_etf_cat['environmental_score']
                ,palette='muted',edgecolor=".9")
    ax7.set_ylabel(ylabel='Environmental score', fontsize=10)
    ax7.set_title(label='ETFs (the ones among the most common categories) - Environmental score', fontsize=12)
    plt.xticks(rotation=30,)#fontsize=10)
    plt.tick_params(labelsize=10, direction='out')
    plt.xlabel('')
    plt.show()
    fig7.set_tight_layout(True)

    fig12,ax12 = plt.subplots(1,1,figsize=(15,15))
    sns.barplot(x=df_mfund_cat['category'],y=df_mfund_cat['environmental_score']
                ,palette='muted',edgecolor='.9')
    ax12.set_ylabel(ylabel='Environmental score', fontsize=10)
    ax12.set_title(label='Mutual Funds (the ones among the most common categories) - Environmental score', fontsize=12)
    plt.xticks(rotation=30,)#fontsize=10)
    plt.tick_params(labelsize=10, direction='out')
    plt.xlabel('')
    plt.tight_layout(True)
    plt.show()

    ###SOCIAL SCORE###
    fig8,ax8 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(y=df_etf_cat['category'],x=df_etf_cat['social_score']
                   ,palette='muted',orient='h')
    #ax8.set_ylabel(ylabel='Social score', fontsize=10)
    ax8.set_title(label='ETFs (the ones among the most common categories) - Social score', fontsize=12)
    #plt.xticks(rotation=45,fontsize=10)
    ax8.set_xlabel('Social score')
    plt.xlim(0,20)
    plt.ylabel('')
    fig8.set_tight_layout(True)
    plt.show()


    fig11,ax11 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(y=df_mfund_cat['category'],x=df_mfund_cat['social_score']
                   ,palette='muted',orient='h')
    #ax11.set_ylabel(ylabel='Social score', fontsize=10)
    ax11.set_title(label='Mutual Funds (the ones among the most common categories) - Social score', fontsize=12)
    ax11.set_xlabel('Social score')
    plt.xlim(0,20)
    #plt.xticks(rotation=45,fontsize=10)
    plt.ylabel('')
    fig11.set_tight_layout(True)
    plt.show()


    ###GOVERNANCE SCORE###
    fig9,ax9 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(y=df_etf_cat['category'],x=df_etf_cat['governance_score']
                ,palette='muted',orient='h')
    #ax9.set_ylabel(ylabel='Governance score', fontsize=10)
    ax9.set_title(label='ETFs (the ones among the most common categories) - Governance score', fontsize=12)
    #plt.xticks(rotation=45,fontsize=10)
    plt.xlabel('Governance score')
    plt.xlim(0,15)
    plt.ylabel('')
    plt.show()
    fig9.set_tight_layout(True)


    fig10,ax10 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(y=df_mfund_cat['category'],x=df_mfund_cat['governance_score']
                ,palette='muted',orient='h')
    #ax10.set_ylabel(ylabel='Governance score', fontsize=10)
    ax10.set_title(label='Mutual Funds (the ones among the most common categories) - Governance score', fontsize=12)
    #plt.xticks(rotation=45,fontsize=10)
    plt.xlabel('Governance score')
    plt.xlim(0,20)
    plt.ylabel('')
    fig10.set_tight_layout(True)
    plt.show()

    #--------------------------------------------------------------------------------------------------------------------------------


    ###MF ETF - year of inception###

    df_etf_date= df_etf['inception_date'].copy()
    df_mfund_date = df_mfund['inception_date'].copy()

    dfetfdate = pd.to_datetime(df_etf_date).apply(lambda x :x.year)
    dfetfdate = dfetfdate[(dfetfdate>=2000) & (dfetfdate<=2020)]
    dfetfdate_val = dfetfdate.value_counts().sort_index()

    dfmfdate=pd.to_datetime(df_mfund_date).apply(lambda x :x.year)
    dfmfdate = dfmfdate[(dfmfdate>=2000) & (dfmfdate<=2020)]
    dfmfdate_val = dfmfdate.value_counts().sort_index()

    labels=dfetfdate_val.index.astype(str)
    hist1 = dfetfdate_val.values
    hist2 = dfmfdate_val.values
    x = np.arange(len(labels))  # the label locations
    width = 0.45  # the width of the bars
    fig15,ax15=plt.subplots(1,1,figsize=(10,10))
    rects1 = ax15.bar(x - width/2, hist1, width, label='ETFs')
    rects2 = ax15.bar(x + width/2, hist2, width, label='Mutual Funds')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax15.set_ylabel('Count')
    ax15.set_title('Mutual Funds vs ETFs - year of inception')
    ax15.set_xticks(x)
    ax15.set_xticklabels(labels)
    ax15.legend(prop={'size': 10})
    # def autolabel(rects):
    #     """Attach a text label above each bar in *rects*, displaying its height."""
    #     for rect in rects:
    #         height = rect.get_height()
    #         ax15.annotate('{}'.format(height),
    #                       xy=(rect.get_x() + rect.get_width() / 2, height),
    #                       xytext=(0, 3),  # 3 points vertical offset
    #                       textcoords="offset points",
    #                       ha='center', va='bottom')
    # autolabel(rects1)
    # autolabel(rects2)
    fig15.tight_layout()
    plt.show()



    #YTD ETF
    fig20,ax20 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(y=df_etf_cat['category'],x=df_etf_cat['fund_trailing_return_ytd']
                ,palette='muted',orient='h')
    ax20.set_xlabel(xlabel='YTD return (%)', fontsize=10)
    ax20.set_title(label='ETFs (the ones among the most common categories) - YTD return ', fontsize=12)
    #plt.xticks(rotation=45,fontsize=10)
    plt.ylabel('')
    plt.show()
    plt.xlim(-80,50)
    fig20.set_tight_layout(True)

    #3YEARS ETF
    fig21,ax21 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(y=df_etf_cat['category'],x=df_etf_cat['fund_trailing_return_3years']
                ,palette='muted',orient='h')
    ax21.set_xlabel(xlabel='3-years return (%)', fontsize=10)
    ax21.set_title(label='ETFs (the ones among the most common categories) - Trailing 3-years return ', fontsize=12)
    #plt.xticks(rotation=45,fontsize=10)
    plt.ylabel('')
    plt.xlim(-50,50)
    fig21.set_tight_layout(True)
    plt.show()

    #5YEARS ETF
    fig22,ax22 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(x=df_etf_cat['category'],y=df_etf_cat['fund_trailing_return_5years']
                ,palette='muted')
    ax22.set_ylabel(ylabel='5-years return (%)', fontsize=10)
    ax22.set_title(label='ETFs (the ones among the most common categories) - Trailing 5-years return ', fontsize=12)
    plt.xticks(rotation=45,fontsize=10)
    plt.show()
    plt.ylim(-50,50)
    fig22.set_tight_layout(True)


    #YTD MF
    fig23,ax23 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(y=df_mfund_cat['category'],x=df_mfund_cat['fund_trailing_return_ytd']
                ,palette='muted',orient='h')
    ax23.set_xlabel(xlabel='YTD return (%)', fontsize=10)
    ax23.set_title(label='Mutual Funds (the ones among the most common categories) - YTD years return ', fontsize=12)
    #plt.xticks(rotation=45,fontsize=10)
    plt.ylabel('')
    plt.xlim(-40,50)
    fig23.set_tight_layout(True)
    plt.show()

    #3years MF
    fig25,ax25 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(y=df_mfund_cat['category'],x=df_mfund_cat['fund_trailing_return_3years']
                ,palette='muted',orient='h')
    ax25.set_xlabel(xlabel='3-years return (%)', fontsize=10)
    ax25.set_title(label='Mutual Funds (the ones among the most common categories) - Trailing 3-years return ', fontsize=12)
    plt.xticks(rotation=45,fontsize=10)
    plt.ylabel('')
    plt.xlim(-40,40)
    fig25.set_tight_layout(True)
    plt.show()

    #5years  MF
    fig26,ax26 = plt.subplots(1,1,figsize=(15,15))
    sns.boxplot(x=df_mfund_cat['category'],y=df_mfund_cat['fund_trailing_return_5years']
                ,palette='muted')
    ax26.set_ylabel(ylabel='5-years return (%)', fontsize=10)
    ax26.set_title(label='Mutual Funds (the ones among the most common categories) - 5 years return ', fontsize=12)
    plt.xticks(rotation=45,fontsize=10)
    plt.show()
    plt.ylim(-50,50)
    fig26.set_tight_layout(True)

    ### DIVIDEND FREQUENCY AMONG THE COMMON ONES ###
    df_etf_div = df_etf_cat_eurgov['dividend_frequency'].dropna()
    df_mfund_div = df_mfund_cat['dividend_frequency'].dropna()

    df_etf_div_val = df_etf_div.value_counts().sort_index()
    df_mf_div_val = df_mfund_div.value_counts().sort_index()

    #histetf_div_keys = df_etf_div_val.index
    #histmf_div_keys=df_mf_div_val.index
    histetf_div_values = df_etf_div_val.values
    histmf_div_values = df_mf_div_val.values

    x_etf = [466,0,9,182,0,0]
    x_mf = histmf_div_values
    labels_div = ['Annually','Four times a year','Monthly','Quarterly','Three times a year','Weekly']
    x_div = np.arange(len(labels_div))  # the label locations
    width = 0.35  # the width of the bars

    fig16,ax16=plt.subplots(1,1,figsize=(10,10))
    rects1 = ax16.bar(x_div - width/2, x_etf, width, label='ETFs',color='green')
    rects2 =  ax16.bar(x_div + width/2, x_mf, width, label='Mutual Funds', color='blue')
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax16.set_ylabel('Count')
    ax16.set_title('Mutual Funds vs ETFs (the ones among the most common categories) - dividend frequency ')
    ax16.set_xticks(x_div)
    ax16.set_xticklabels(labels_div)
    ax16.legend(prop={'size': 15})
    # def autolabel(rects):
    #     """Attach a text label above each bar in *rects*, displaying its height."""
    #     for rect in rects:
    #         height = rect.get_height()
    #         ax16.annotate('{}'.format(height),
    #                       xy=(rect.get_x() + rect.get_width() / 2, height),
    #                       xytext=(0, 3),  # 3 points vertical offset
    #                       textcoords="offset points",
    #                       ha='center', va='bottom')
    # autolabel(rects1)
    # autolabel(rects2)
    fig16.tight_layout()
    plt.show()


























