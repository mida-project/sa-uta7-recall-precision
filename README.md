# Recall &amp; Precision Problem UTA7 Statistical Analysis

<img src="https://github.com/mida-project/meta/blob/master/banners/statistical-analysis.png?raw=true" width="100%" />

[![MIT](https://flat.badgen.net/github/license/mida-project/sa-uta7-recall-precision)](https://github.com/mida-project/sa-uta7-recall-precision/blob/master/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/mida-project/sa-uta7-recall-precision?style=flat-square)](https://github.com/mida-project/sa-uta7-recall-precision/commits/master)
[![HitCount](http://hits.dwyl.io/mida-project/sa-uta7-recall-precision.svg)](http://hits.dwyl.io/mida-project/sa-uta7-recall-precision)
[![OpenCollective](https://opencollective.com/oppr/backers/badge.svg?style=flat-square)](#backers)
[![OpenCollective](https://opencollective.com/oppr/sponsors/badge.svg?style=flat-square)](#sponsors)
[![Gitter](https://img.shields.io/gitter/room/gitterHQ/gitter.svg?style=flat-square)](https://gitter.im/opprTeam)
[![Twitter](https://flat.badgen.net/twitter/follow/opprGroup)](https://twitter.com/opprGroup)

This repository aims to assemble a set of [`methods/`](methods/) for our statistical analysis of the [Recall &amp; Precision](https://dspace2.flinders.edu.au/xmlui/bitstream/handle/2328/27165/Powers%20Evaluation.pdf?sequence=1&isAllowed=y) problem from [UTA7](https://github.com/MIMBCD-UI/prototype-breast-screening/wiki/User-Research#test-7-multi-modality-vs-assistant-chi2020-). For the purpose, we are computing several heatmaps representing our **[Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix)** (or **[Error Matrix](https://en.wikipedia.org/wiki/Confusion_matrix)**). In a nutshell, a **[Confusion Matrix](https://en.wikipedia.org/wiki/Confusion_matrix)** is a short description of prediction results on a classification problem. In our [publications](https://github.com/BreastScreening/meta/wiki/Publications), we are measuring the frequency of these predictions for our *[datasets](https://github.com/BreastScreening/meta/wiki/Datasets)*. The *[datasets](https://github.com/BreastScreening/meta/wiki/Datasets)* are representing our [Machine Learning](https://en.wikipedia.org/wiki/Machine_learning) prediction results of the [BIRADS](http://www.radiologyassistant.nl/en/p53b4082c92130/bi-rads-for-mammography-and-ultrasound-2013.html) values on [breast cancer](https://www.breastcancer.org/). From here, we will address the [Recall &amp; Precision](https://dspace2.flinders.edu.au/xmlui/bitstream/handle/2328/27165/Powers%20Evaluation.pdf?sequence=1&isAllowed=y) problem. But first, lets shortly explain each. **Recall** is the ration for the total number of correctly classified positive [BIRADS](http://www.radiologyassistant.nl/en/p53b4082c92130/bi-rads-for-mammography-and-ultrasound-2013.html) values divided by the total number of predicted positive [BIRADS](http://www.radiologyassistant.nl/en/p53b4082c92130/bi-rads-for-mammography-and-ultrasound-2013.html) samples. On the other hand, **Precision** is the total number of correctly classified positive [BIRADS](http://www.radiologyassistant.nl/en/p53b4082c92130/bi-rads-for-mammography-and-ultrasound-2013.html) samples divided by the total number of predicted positive [BIRADS](http://www.radiologyassistant.nl/en/p53b4082c92130/bi-rads-for-mammography-and-ultrasound-2013.html) examples.

> Often, we think that precision and recall both indicate accuracy of the model. While that is somewhat true, there is a deeper, distinct meaning of each of these terms. Precision means the percentage of your results which are relevant. On the other hand, recall refers to the percentage of total relevant results correctly classified by your algorithm. Undoubtedly, this is a hard concept to grasp in the first go. So, let me try to explain it with Jack’s example.

In "*[Precision vs Recall](https://towardsdatascience.com/precision-vs-recall-386cf9f89488)*", May 11, 2018 on [Medium](https://medium.com/) at the [Towards Data Scienc](https://towardsdatascience.com/) channel.

&#8212; [Shruti Saxena](https://towardsdatascience.com/@shrutisaxena0617)

The hereby repository is dependent from the [`sheet-reader`](https://github.com/MIMBCD-UI/sheet-reader) repository, so please first of all clone that to your machine. The work is submitted to top [Human-Computer Interaction (HCI)](https://www.interaction-design.org/literature/topics/human-computer-interaction) conferences of [Computer Science (CS)](http://www.guide2research.com/). For more information regarding our results, please follow our set of [`notebooks/`](src/notebooks/). You can start by the [`confusions.ipynb`](src/notebooks/confusions.ipynb) file, for example. In the repository [wiki](https://github.com/mida-project/sa-uta7-recall-precision/wiki) we further address several other questions and results.

<a href="https://www.patreon.com/oppr" target="_blank">
<img src="https://c5.patreon.com/external/logo/become_a_patron_button@2x.png" width="160">
</a>

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
python3 src/core/main.py
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

## Supporting

Our organization is a non-profit organization. However, we have many needs across our activity. From infrastructure to service needs, we need some time and contribution, as well as help, to support our team and projects.

<span class="image">
  <a href="https://opencollective.com/oppr" target="_blank">
    <img src="https://opencollective.com/oppr/tiers/backer.svg" width="220">
  </a>
</span>

### Contributors

This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)].

<span class="image">
  <a href="graphs/contributors">
    <img src="https://opencollective.com/oppr/contributors.svg?width=890" />
  </a>
</span>

### Backers

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/oppr#backer)]

<span class="image">
  <a href="https://opencollective.com/oppr#backers" target="_blank">
    <img src="https://opencollective.com/oppr/backers.svg?width=890">
  </a>
</span>

### Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/oppr#sponsor)]

<span class="image">
  <a href="https://opencollective.com/oppr/sponsor/0/website" target="_blank">
    <img src="https://opencollective.com/oppr/sponsor/0/avatar.svg">
  </a>
</span>

<br />

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

#### Departments

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

#### Laboratories

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
    <img src="https://github.com/mida-project/meta/blob/master/brands/iti_footer.png" alt="iti" width="20%" />
  </a>
</span>
<span class="image">
  <a href="http://www.inesc-id.pt/" title="INESC-ID" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/inesc-id_footer.png" alt="inesc-id" width="20%" />
  </a>
</span>

#### Domain

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
