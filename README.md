# Recall &amp; Precision Problem UTA7 Statistical Analysis

<img src="https://github.com/mida-project/meta/blob/master/banners/statistical-analysis.png?raw=true" width="100%" />

This repository aims to assemble a set of [`methods/`](methods/) for our statistical analysis of the [Recall &amp; Precision Problem](https://dspace2.flinders.edu.au/xmlui/bitstream/handle/2328/27165/Powers%20Evaluation.pdf?sequence=1&isAllowed=y) from [UTA7](https://github.com/MIMBCD-UI/prototype-breast-screening/wiki/User-Research#test-7-multi-modality-vs-assistant-chi2020-). We use several statistical models (e.g.: [ANOVA](https://en.wikipedia.org/wiki/Analysis_of_variance), [Kruskal-Wallis One-Way Analysis of Variance](https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_one-way_analysis_of_variance), [Mann-Whitney U test](https://en.wikipedia.org/wiki/Mann%E2%80%93Whitney_U_test), etc...) to analyse our data and deeper understanding it. For instance, we used the [Kruskal-Wallis One-Way Analysis of Variance](https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_one-way_analysis_of_variance) for our [ISS'17](https://iss2017.acm.org/) Publications ([Paper](https://dl.acm.org/citation.cfm?id=3134111) & [Poster](https://iss2017.acm.org/program/posters/#iss43-ex)), analyzing the **Results** of our data. The hereby repository is dependent from the [`sheet-reader`](https://github.com/MIMBCD-UI/sheet-reader) repository, so please first of all clone that to your machine. The work is submitted to top [Human-Computer Interaction (HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction) conferences of [Computer Science (CS)](http://www.guide2research.com/). Results will be published on both [Current vs Assistant](https://www.overleaf.com/project/5d07b177aa894d7b4d4638e4) ([CHI 2020](https://chi2020.acm.org/)) and [Human-AI Interactions](https://www.overleaf.com/project/5d07b177aa894d7b4d4638e4) ([IUI 2020](https://iui.acm.org/2020/)) papers for higher context.

## Pre-Requisites

To run the various methods available on the `src/methods/` directory, it is needed:

- [Python 2.6](https://www.python.org/download/releases/2.6/) or [latest](https://www.python.org/downloads/);

- The [pip](https://pypi.org/project/pip/) package management tool;

- The [`sheet-reader`](https://github.com/MIMBCD-UI/sheet-reader) (>= [v1.2.1](https://github.com/MIMBCD-UI/sheet-reader/releases/tag/v1.2.1) version) repository;

## Instructions

The instructions are as follows. We assume that you already have knowledge over [Git](https://git-scm.com/) and [GitHub](https://github.com/). If not, please follow this [support](https://guides.github.com/activities/hello-world/) information. Any need for support, just open a [New issue](https://github.com/MIMBCD-UI/statistical_analysis/issues/new).

### Clone

To clone the hereby repository follow the guidelines. It is easy as that.

1.1. Please clone the repository by typing the command:

```
git clone https://github.com/MIMBCD-UI/sa-uta7-recall-precision.git
```

1.2. Get inside of the repository directory:

```
cd sa-uta7-recall-precision/
```

1.3. For the installation and running of the source code, follow the next steps;

### Install

The installation guidelines are as follows. Please, be sure that you follow it correctly.

2.1. Run the following command to install the [library](https://github.com/google/google-api-python-client) using [pip](https://pypi.org/project/pip/):

```
pip install --upgrade google-api-python-client
```

2.2. Follow the next step;

### Run

The running guidelines are as follows. Please, be sure that you follow it correctly.

3.1. Run the sample using the following command:

```
python3 src/methods/anova.py
```

3.2. Enjoy our source code!

### Notebooks

You can also run a Notebook to watch some of our `methods` chart plots. For this goal we are using the well known [Jupyter Notebook](http://jupyter.org/) web application. To run the [Jupyter Notebook](http://jupyter.org/) just follow the steps.

4.1. Get inside our project directory:

```
cd sa-uta7-recall-precision/
```

4.2. Run [Jupyter Notebook](http://jupyter.org/) application by typing:

```
jupyter notebook
```

> If you have any question regarding the [Jupyter Notebook](http://jupyter.org/) just follow their [Documentation](http://jupyter.org/documentation). You can also ask for help close to the [Community](http://jupyter.org/community).

## Information

As far as we have to do several statictical analysis over our users, we need to address their results by calculating a set of measures. This measures will gave us a better understanding regarding how users are aiming to interact with our systems. Therefore it is of chief importance to scale this solution for a spreadsheet template-like where we can duplicate the same document and apply this group of source code to consume our data each time we need it.

### Related Repositories

The following list, represents the set of related repositories for the presented one:

- [`sheet-reader`](https://github.com/MIMBCD-UI/sheet-reader)

- [`statistical-analysis`](https://github.com/MIMBCD-UI/statistical-analysis)

- [`uta7-statistical-analysis-charts`](https://github.com/mida-project/uta7-statistical-analysis-charts)

### Dataset Resources

For the [User Test Analysis 7 (UTA7)](https://github.com/MIMBCD-UI/prototype-breast-screening/wiki/User-Research#test-7-multi-modality-vs-assistant-chi2020-) of this project we generated a combination of interesting [datasets](https://www.kaggle.com/MIMBCD-UI/uta4-sm-vs-mm-sheets). To publish our [datasets](https://www.kaggle.com/MIMBCD-UI) we used a well known platform called [Kaggle](https://www.kaggle.com). To access our project's [Profile Page](https://www.kaggle.com/MIMBCD-UI) just follow the [link](https://www.kaggle.com/MIMBCD-UI). We are also working on several other [User Research](https://github.com/MIMBCD-UI/prototype-breast-screening/wiki/User-Research) studies, while this repository is being an important asset to them.

### Acknowledgements

We would like to convey [Google](https://google.com) from their [Google Sheets API Documentation](https://developers.google.com/sheets/api/guides/concepts). This repository source code is based on [Google](https://google.com)'s [Python Quickstart](https://developers.google.com/sheets/api/quickstart/python) guide.

### Authors

- [Francisco Maria Calisto](http://www.franciscocalisto.me/) [[ResearchGate](https://www.researchgate.net/profile/Francisco_Maria_Calisto) | [GitHub](https://github.com/FMCalisto) | [Twitter](https://twitter.com/FMCalisto) | [LinkedIn](https://www.linkedin.com/in/fmcalisto/)]

## Sponsors

<span class="image">
  <a href="http://www.fct.pt/" title="FCT" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/fct_footer.png" alt="fct" width="20%" />
  </a>
</span>
<span class="image">
  <a href="https://www.fccn.pt/en/" title="FCCN" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/fccn_footer.png" alt="fccn" width="20%" />
  </a>
</span>
<span class="image">
  <a href="https://www.ulisboa.pt/en/" title="ULisboa" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/ulisboa_footer.png" alt="ulisboa" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://tecnico.ulisboa.pt/" title="IST" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/ist_footer.png" alt="ist" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://hff.min-saude.pt/" title="HFF" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/hff_footer.png" alt="hff" width="20%" />
  </a>
</span>

## Departments

<span class="image">
  <a href="http://dei.tecnico.ulisboa.pt" title="DEI" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/dei_footer.png" alt="dei" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://deec.tecnico.ulisboa.pt" title="DEEC" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/deec_footer.png" alt="dei" width="20%" />
  </a>
</span>

## Laboratories

<span class="image">
  <a href="http://sipg.isr.tecnico.ulisboa.pt/" title="SIPG" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/sipg_footer.png" alt="sipg" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://welcome.isr.tecnico.ulisboa.pt/" title="ISR" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/isr-lisboa_footer.png" alt="isr" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://larsys.pt/" title="LARSys" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/larsys_footer.png" alt="larsys" width="20%" />
  </a>
</span>
<span class="image">
  <a href="https://www.m-iti.org/" title="M-ITI" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/iti_footer.png" alt="inesc-id" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://www.inesc-id.pt/" title="INESC-ID" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/inesc-id_footer.png" alt="inesc-id" width="20%" />
  </a>
</span>

## Domain

<span class="image">
  <a href="https://europa.eu/" title="EU" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/eu_footer.png" alt="eu" width="20%" />
  </a>
</span>
<span class="image">
  <a href="https://www.portugal.gov.pt/" title="Portugal" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/pt_footer.png" alt="pt" width="20%" />
  </a>
</span>