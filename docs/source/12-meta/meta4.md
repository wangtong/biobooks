# 12.4 为什么宏基因组测序比较难？

**1 样品采集：**

由于微生物在地球上广泛的覆盖，因此，宏基因组样品来源非常广泛，从南北极冰川，到海底淤泥，从喜马拉雅山山脉，到亚马逊丛林，覆盖高山，大河，冰川，土壤，海洋，大气，火山，牛胃，包括人体各个部分都可以进行宏基因组研究，采集到合适的样品，才能开展创新性的研究。

**2 样品提取：**

由于微生物宏基因组样品种类繁多，可以来自人肠道，山川，河流，土壤，粪便等等样品。因此，很难有统一的样品提取流程。往往无法提取到高质量的DNA而影响后续分析结果。另外，由于样品中可能包括多种物种，例如革兰氏阳性菌和革兰氏阴性菌，由于二者细胞壁的差别，不同的提取方法都可能造成差异。另外，一些样品中可能包含宿主污染，去除宿主污染也是一大难题。对于宏转录样品，由于原核生物与真核生物 RNA结构不同，也不能采用同样的测序。样品提取一直是宏基因组分析中一项重大难题，需要结合前人经验，以及具体样品，不停的摸索经验。

**3 建库方案：**

选择不同的建库方案，会对结果造成影响。二代测序需要使用PCR扩增，会带来PCR的偏向性，比如高GC区域无法很好的扩增出来，测序不到，影响后续分析。宏基因组样品由于包含多种GC含量微生物，不同的建库方案会带来差异。

**4 测序成本：**

尽管随着测序技术的发展，测序价格越来越低。当前测序成本已经下降很多。人全基因组价格已经突破1000美金。但是因为宏基因组测序量数据量大，比如二代测序，每个样本要达到6G以上数据，因此，进行大规模研究，成本依然很高。除了测序费用，后续数据存储，传输，计算等都是不小的费用。

**5 测序技术条件限制：**

虽然现在的测序技术实现了高通量，可以一次测序环境样品中全部序列。但由于测序读长短，存在测序错误，特异性差，对于物种分类鉴定，基因组拼接都会产生很大的影响。例如，无法完整拼接出样品中包含的全部，完整微生物基因组序列。

**6 数据分析：**

当前技术条件下，分析单个细菌或者真菌也具有很大的难度。而宏基因组包含未知种类和数目的微生物，并且由于宏基因组测序数据量较大，分析难度也水涨船高。宏基因组数据分析需要微生物学，计算机，统计学等基础。宏基因组分析方法，软件，算法非常多，数据处理过程复杂，分析难度较大。并且很多时候没有标准作为参考，只能摸石头过河。

**7 计算资源：**

由于宏基因组样品测序量较大，二代测序单个样品一般都需要6G数据以上，有些更多。给数据的存储，传输，计算，分享带来很大困难。物种鉴定，基因组拼接都需要非常大的计算资源，例如多核心CPU（32线程以上），较大的内存（256G内存以上）。计算资源目前依然是宏基因组分析中的瓶颈，很多实验室缺乏足够的计算资源来处理宏基因组数据。另外，由于计算时间较长，不方便反复调整选项参数，得到最优解。

**8 数据库完整性：**

宏基因组物种鉴定完全依赖已知数据库信息。数据库的完整性直接影响到最终分析结果。当前技术条件下，只测序了一小部分微生物。因此，宏基因组物种鉴定中，还会有大量物种无法鉴定，即使鉴定出没有达到种水平。另外，数据库中结果的准确性也直接影响到鉴定结果。之前一些物种分类错误，这样的问题得不到修正，会逐渐累积下去。

**9 相似物种的干扰：**

宏基因组样本是一个微生物的混合群落，里面的物种会有来自同一种或者同一属及以上水平的物种，这些物种基因组序列具有相似性，比如基因组同源性达到70%。这会给物种鉴定时测序数据分配，基因组组装测序数据连接造成干扰。例如测序数据分配错误，造成丰度偏差，基因组拼接形成嵌合体序列等，影响分析结果，造成假阳性。

**10 结果可重复性：**

由于以上宏基因组分析中诸多的影响条件，从样品采集，保存，提取，建库，测序，不同的数据量，选用不同软件，算法，数据库等，都会产生干扰，因此，同样的样品，结果不容易重复。