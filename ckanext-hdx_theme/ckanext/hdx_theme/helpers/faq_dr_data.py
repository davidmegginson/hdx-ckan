section_1 = {
    'title': 'Section 1',
    'questions': [
        {
            'q': 'What are some basic health data management precautions that all organizations should take in the '
                 'COVID-19 response?',
            'a': 'The World Health Organization recommends the following measures to ensure the ethical and secure use '
                 'of data: '
                 '<ol>'
                 '<li> Use anonymization and other tools as appropriate. </li>'
                 '<li> Comply with informed consent agreements where such consent is needed and respect assurances '
                 'about ways in which the data (anonymized or otherwise) would be used, shared, stored or protected. '
                 '</li> '
                 '<li> Adopt appropriate security measures to foster public trust. </li>'
                 '<li> Any platforms established to share data should have an explicit ethical framework governing '
                 'data collection and use. </li>'
                 '</ol>'
                 'In addition, consider the following:'
                 '<ol>'
                 '<li> Ensure adequate de-identification of data within health data management activities. '
                 'Consult relevant guidance to determine which tool is most appropriate for de-identification of the '
                 'type of data you\'re handling when using digital (communication) technologies in healthcare, data '
                 'protection is paramount. Determine which tools are used by healthcare professionals and only use '
                 'tools that allow for the appropriate level of encryption. </li>'
                 '<li> Clearly define the purpose of data management, measures for data minimisation and limitation of '
                 'data retention, and the specific roles and responsibilities of different stakeholders throughout the '
                 'data management process. This should include a clear overview of which parties are responsible for '
                 'safeguarding data at different stages. '
                 '</li> '
                 '<li> When sharing data with specific recipients, be transparent regarding the appropriate use of the '
                 'data, and make sure this is compatible with the original purpose for which the data was collected. '
                 '</li>'
                 '<li> Data can be vulnerable to interception at points of transfer between different organizations. '
                 'Additionally, data may be misused intentionally or unintentionally after the transfer. Select the '
                 'right method and tool for transfer, and to stipulate the licence or terms under which data may be '
                 'used in a clear manner (see '
                 '<a href="/faq-data-responsibility-covid-19#auto-faq-Section_1-What_are_the_different_licenses_available_for_data_sharing_and_what_do_they_cover_-q">"What are the different licenses available for data '
                 'sharing and what do they cover?"</a> for more information on this point). </li>'
                 '</ol>'
                 'Following these best practices will help ensure responsible data management in the COVID-19 response.'
            ,
        },
        {
            'q': 'What constitutes sensitive data generally and in the health sector specifically?',
            'a': '<p> Any data that may put certain individuals, groups or organizations at risk of harm in a '
                 'particular context should be considered sensitive. While personal data can categorically be '
                 'considered sensitive, more nuanced issues arise for non-personal data. For example, locations of '
                 'medical facilities in conflict settings can expose patients and staff to risk, while the same data '
                 'would not necessarily be considered sensitive in a natural disaster response context. </p>'
                 '<p> In the health sector specifically, all identifiable data concerning health, factors influencing '
                 'health (for example, cultural and socio-economic details) and the history of individuals are '
                 'sensitive and must be handled with care and professionalism. In addition, any data (identifiable or '
                 'not) that can be voluntarily or involuntarily misused against the interests of patients, potential '
                 'patients, their family, groups or communities and/or health service providers or other humanitarian '
                 'organizations and their staff, or put any of them at risk for political reasons, financial gain or '
                 'any other reasons shall be treated as "highly sensitive" data. Even some seemingly non-sensitive '
                 'data can be highly sensitive in certain contexts (for example, details of cholera outbreaks). '
                 'Finally, the metadata generated as a \'byproduct\' of data management can create a distinct set of '
                 'risks, which should not be overlooked. For more information on the risks associated with metadata, '
                 'see '
                 '<a href="https://www.icrc.org/en/document/digital-trails-could-endanger-people-receiving-humanitarian-aid-icrc-and-privacy" target="_blank"> https://www.icrc.org/en/document/digital-trails-could-endanger-people-receiving-humanitarian-aid-icrc-and-privacy</a> '
                 '</p>'
            ,
        },
        {
            'q': 'What are some common types of sensitive data in the COVID-19 response?',
            'a': 'In the COVID-19 response, the following common data types may be considered sensitive and should be '
                 'treated with care:'
                 '<ol>'
                 '<li> any identifiable data </li>'
                 '<li> non-identifiable data on sensitive topics, including but not limited to: violence related '
                 'injuries; rape; termination of pregnancy; patients in prisons or detention centers;</li> '
                 '<li> information on the disease in a context where there is an obligation to abide by treatment or '
                 'other related measures, such as quarantine; </li>'
                 '<li> non-identifiable data which reveals or implies racial or ethnic origin, political opinions, '
                 'religious or philosophical beliefs, offences or sex life or preferences. </li>'
                 '</ol>'
                 '<p> Assessing the sensitivity of data requires a clear understanding of the context and the different'
                 ' ways in which data may lead to harm. Data Sensitivity Classifications such as '
                 '<a href="https://docs.google.com/document/d/1FYI9n2NcQAUTC-0XlQ5drPcYwfY_OXPRvaU0KMuMzHQ/edit" target="_blank">this example</a>'
                 ' (from '
                 'the working draft '
                 '<a href="https://centre.humdata.org/wp-content/uploads/2019/03/OCHA-DR-Guidelines-working-draft-032019.pdf" target="_blank">OCHA Data Responsibility Guidelines</a>'
                 ') can help humanitarian organizations '
                 'consistently assess and manage data sensitivity in different environments. </p>'
                 '<p> These classifications can be developed at the country level and/or at the sector/cluster level '
                 'where necessary (e.g. the health cluster may wish to establish a sensitivity classification specific '
                 'to data required for COVID-19 response interventions in certain contexts). Humanitarians operating '
                 'at the National or Sub-National level are encouraged to engage with the appropriate partners and '
                 'coordinating bodies to ensure data management is conducted according to relevant standards for IM '
                 'services in public health. This includes aligning with existing context-specific data sensitivity '
                 'classifications.</p>'
            ,
        },
        {
            'q': 'What measures can I take to uphold data privacy and reduce the risk of re-identification of '
                 'individuals and groups before publishing data?',
            'a': '<p> Data on the characteristics of units of a population (e.g. individuals, households or '
                 'establishments) collected by a census, survey or experiment is referred to in statistics as '
                 '\'microdata\'. In humanitarian response, this type of data is gathered through exercises such as '
                 'household surveys, needs assessments, and other programme monitoring activities. Such data make up '
                 'an increasingly significant volume of data in the humanitarian sector, and will play a key role in '
                 'the COVID-19 response. </p>'
                 '<p> In its raw form, microdata can contain both personal data and non-personal data on a range of '
                 'topics. Most humanitarian organisations acknowledge the sensitivity of personal data such as names, '
                 'biometric data, or ID numbers and anonymise data sets accordingly as a matter of standard practice. '
                 'However, it is often still possible to re-identify individual respondents or groups by combining '
                 'answers to different questions, even after such \'anonymisation\' is applied. </p>'
                 '<p> Depending on the type of data you\'re managing, there are various tools available to determine '
                 'and reduce the risk of re-identification in the data. For microdata, one such approach is '
                 'Statistical Disclosure Control (SDC). </p>'
                 '<p> SDC is a technique used to assess and lower the risk of a person or organization being '
                 're-identified from the analysis of microdata (data on the characteristics of a population). The '
                 'purpose of applying disclosure control to microdata is to be able to share the data more widely '
                 'in a responsible manner. An SDC process can lower the risk of re-identification to an acceptable '
                 'level but the risk threshold may vary depending on the context to which the data relates. '
                 'There are a variety of free and open source tools available for conducting SDC, including '
                 '<a href="https://ihsn.org/software/disclosure-control-toolbox" target="_blank">sdcMicro</a>. '
                 'Read this '
                 '<a href="https://centre.humdata.org/wp-content/uploads/2019/07/guidance_note_sdc.pdf" '
                 'target="_blank">guidance note</a> from the Centre for Humanitarian Data for more information '
                 'on how to start using SDC. </p>'
            ,
        },
        {
            'q': 'What are the existing standards for surveillance and case definition and reporting?',
            'a': '<p> The World Health Organization has published '
                 '<a href="https://www.who.int/emergencies/diseases/novel-coronavirus-2019/technical-guidance/surveillance-and-case-definitions" target="_blank">technical guidance on surveillance and case '
                 'definitions for COVID-19</a>. This guidance includes resources for use in case-based reporting -- '
                 'including a Case-based reporting form, a Data dictionary for case-based reporting form, and '
                 'Template for Line list for case-based reporting -- as well as aggregated reporting, including an '
                 'Aggregated weekly reporting form. </p>'
            ,
        },
        {
            'q': 'Where can I find the latest data about the ongoing COVID-19 emergency?',
            'a': '<p> The World Health Organization maintains a real-time dashboard providing an overview of the '
                 'COVID-19 situation here '
                 '<a href="https://experience.arcgis.com/experience/685d0ace521648f8a5beeeee1b9125cd" target="_blank">https://experience.arcgis.com/experience/685d0ace521648f8a5beeeee1b9125cd</a>'
                 ' </p>'
                 '<p> Their data is updated live and can be accessed here: '
                 '<a href="https://data.humdata.org/dataset/coronavirus-covid-19-cases-data-for-china-and-the-rest-of-the-world" target="_blank">https://data.humdata.org/dataset/coronavirus-covid-19-cases-data-for-china-and-the-rest-of-the-world</a>'
                 ' </p>'
                 '<p> A number of humanitarian organizations are publishing data about different aspects of the global '
                 'and country-level response to COVID-19. Many of these resources are available in a dedicated '
                 '<a href="https://data.humdata.org/event/covid-19">COVID-19 crisis page on the Humanitarian Data Exchange</a>'
                 '. </p>'
                 '<p> Many national health authorities also provide updates on a daily basis. Visit your national '
                 'health authority\'s website for more information. </p>'
            ,
        },
        {
            'q': 'How can I determine the most appropriate method and/or tool for sharing or otherwise transferring '
                 'data in a secure way?',
            'a': '<p> Consult the relevant guidance or focal point within your organization to see which methods and '
                 'tools are considered appropriate for the secure transfer of (sensitive) data. In general, a secure '
                 'method or tool will enable encryption of the data in transit and at rest, offer secure '
                 'authentication functionality and access restrictions, among other security features. For example, '
                 'most email service providers allow you to turn on encryption of emails and their attachments. </p>'
            ,
        },
        {
            'q': 'What are the different licenses available for data sharing and what do they cover?',
            'a': '<p> Licenses stipulate the terms under which data is shared. This means that a license will describe '
                 'how data may be used and shared further, as well as any attribution to the original source that '
                 'should take place. A list of commonly used licenses is available here: '
                 '<a href="https://data.humdata.org/about/license">https://data.humdata.org/about/license</a> </p>'
            ,
        },
        {
            'q': 'How can my organization ensure responsible data practice when developing or using models in the '
                 'COVID-19 response?',
            'a': '<p> Epidemic models are an essential tool in the hands of governments and policy makers for planning '
                 'and responding to COVID-19. This crisis shows how predictive analytics can inform and maximise the '
                 'impact of interventions, especially in resource-limited contexts. It also shows the importance of '
                 'having models that are validated and ready to be deployed right before or at the beginning of a '
                 'crisis. </p>'
                 'Unfortunately, translating the outputs of predictive models into timely and appropriate responses in'
                 ' the humanitarian sector remains a challenge for several reasons:'
                 '<ol>'
                 '<li> First, there is no common standard for documenting predictive models and their intended use '
                 'which highlights the critical aspects for the application of models in the humanitarian sector. </li>'
                 '<li> Second, there is no common standard or mechanism for assessing the technical rigor and '
                 'operational readiness of predictive models in the sector. </li> '
                 '<li> Third, the development of predictive models is often led by technical specialists who may not '
                 'consider important ethical concerns that the application of models in humanitarian contexts '
                 'may entail. </li>'
                 '</ol>'
                 '<p> One approach for addressing these challenges is to submit models for peer review. The Centre for '
                 'Humanitarian Data recently published an updated version of its '
                 '<a href="https://centre.humdata.org/wp-content/uploads/2020/03/peer-review-framework-2020.pdf" target="_blank">Peer Review Framework for Predictive Analytics in Humanitarian Response</a>'
                 '. The Framework aims to create standards and processes for the use of models in our sector. It is '
                 'based on research with experts and stakeholders across a range of organizations that design and use '
                 'predictive models. The Framework also draws on best practices from academia and the private sector. '
                 '</p>'

            ,
        },
        {
            'q': 'What policies and guidelines currently exist to inform the management of data in public '
                 'health emergencies? ',
            'a': '<p> Many individual organizations have policies and guidelines specific to the safe, ethical, and '
                 'effective management of different types of data. Institutional policies on personal data protection '
                 'are particularly relevant to the responsible management of health data and should serve as a '
                 'primary reference for staff in the COVID-19 response. </p>'
                 '<p> In addition, many national and regional authorities have included provisions specific to '
                 'health data management in national and regional data protection legislation and other relevant '
                 'regulatory frameworks. National laws on medical practice may also include specific rules on '
                 'health data management. Consult a local legal professional to ensure you are aware of and abide by '
                 'all applicable data protection laws. </p>'
                 '<p> The World Health Organization '
                 '<a href="https://www.who.int/wer/2016/wer9118.pdf?ua=1" target="_blank">Policy statement on data sharing by WHO in the context of public health emergencies (as of 13 April 2016)</a>'
                 ' and '
                 '<a href="" target="_blank">Guidance on good data and record management practices</a>'
                 ' are the primary global frameworks of reference for the management of data in public health '
                 'emergencies.  </p>'
                 '<p> The Global Health Cluster '
                 '<a href="https://www.who.int/health-cluster/resources/publications/Final-PHIS-Standards.pdf" target="_blank">Standards for Public Health Information Services in Activated Health Clusters and other Humanitarian Health Coordination Mechanisms</a>'
                 ' should also serve as a key reference for humanitarian practitioners. Although this document refers '
                 'to Public Health Information Services (PHIS) in activated health clusters (HCs), these PHIS '
                 'Standards are by no means restricted to health clusters, and can be applied to support government '
                 'led emergency coordination or other types of humanitarian sectoral coordination mechanisms. </p>'
                 '<p> The WHO '
                 '<a href="https://www.who.int/publishing/datapolicy/Policy_data_sharing_non_emergency_final.pdf" target="_blank">\'Policy on the use and sharing of data collected in Member States by the WHO, outside the context of public health emergencies\'</a>'
                 ' contains '
                 '<a href="https://www.who.int/about/who-we-are/publishing-policies/data-policy" target="_blank">extensive annexes on security, safeguards, ethics and guidance</a>'
                 ' on implementation and may also serve as a helpful reference. However, the policy excludes data '
                 'shared in the context of public health emergencies, including Public Health Emergencies of '
                 'International Concern (such as the COVID-19 pandemic) and data and reports from clinical trials and '
                 'biological samples, and data collected by WHO prior to policy implementation. </p>'
                 '<p> While there are a number of different sets of principles related to the responsible management '
                 'of data in public health, international development and humanitarian action, the most directly '
                 'relevant here are the '
                 '<a href="https://www.go-fair.org/fair-principles/" target="_blank">FAIR data principles</a>'
                 ' and the '
                 '<a href="https://www.unsystem.org/personal-data-protection-and-privacy-principles" target="_blank">United Nations Privacy Policy Group Personal Data Protection and Privacy Principles</a>. </p>'
                 '<p> When data is used for purposes other than informing the response (e.g. research), '
                 'additional frameworks and principles may apply. Researchers should refer to the '
                 '<a href="https://www.who.int/about/ethics/code-of-conduct-for-responsible-research" target="_blank">WHO Code of Conduct for responsible Research</a>'
                 ', which provides standards of good practice to guide individuals working on all research associated '
                 'with WHO, including non-clinical research, in line with the principles of integrity, accountability,'
                 ' independence/impartiality, respect and professional commitment described in '
                 '<a href="https://www.who.int/about/ethics/code_of_ethics_full_version.pdf?ua=1" target="_blank">WHO\'s Code of Ethics and Professional Conduct</a>'
                 '. </p>'
            ,
        },
        {
            'q': 'Where can I learn more about data responsibility in humanitarian situations and in public '
                 'health programming?',
            'a': '<p> Data responsibility entails a set of principles, processes and tools that support the safe, '
                 'ethical and effective management of data in humanitarian response. This includes data privacy, '
                 'protection, and security, as well as other practical measures to mitigate risk and prevent harm. </p>'
                 'There is a wealth of guidance available on how to responsibly manage data in public health '
                 'emergencies and in humanitarian action more generally that should inform data management in the '
                 'COVID-19 response. The following resources provide additional information and guidance on the safe, '
                 'ethical, and effective management of data in humanitarian action: '
                 '<ol>'
                 '<li> <a href="https://www.accessnow.org/cms/assets/uploads/2020/03/Access-Now-recommendations-on-Covid-and-data-protection-and-privacy.pdf" target="_blank">Recommendations on privacy and data protection in the fight against COVID-19 (Access Now)</a> </li>'
                 '<li> <a href="https://www.icrc.org/en/publication/handbook-data-protection-humanitarian-action" target="_blank">Handbook on Data Protection in Humanitarian Action (ICRC and Brussels Privacy Hub)</a> </li> '
                 '<li> <a href="https://centre.humdata.org/wp-content/uploads/2019/03/OCHA-DR-Guidelines-working-draft-032019.pdf" target="_blank">Working Draft Data Responsibility Guidelines (OCHA Centre for Humanitarian Data)</a> </li>'
                 '<li> <a href="https://www.measureevaluation.org/resources/publications/ms-17-125a" target="_blank">mHealth Data Security, Privacy, and Confidentiality: Guidelines for Program Implementers and Policymakers</a> </li>'
                 '</ol>'
                 '<p> For a broad range of resources related to data responsibility in development and humanitarian '
                 'work, consult the '
                 '<a href="https://docs.google.com/document/d/1Fa2QHusD5iJ8Woi8s7-SMFItAufKv4U5UR-PZ1szMNU/edit#heading=h.k5ayqcygtlml" target="_blank">Responsible Data Resource List</a>'
                 ' maintained by MERL Tech and the Engine Room.  </p>'
            ,
        },
    ]
}


faq_dr_data = [
    section_1
]
