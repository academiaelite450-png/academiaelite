import { useState } from "react";

const slides = [
  {
    type: "title",
    content: {
      title: "Examining Customer Satisfaction with AI-Powered Chatbots in UK Retail Banking",
      subtitle: "A Study of NatWest's Cora",
      meta: [
        "MBA7067 – Professional Project",
        "Student: [Your Name] | Student ID: [Your ID]",
        "Tutor: Dr. Maria Busen-Smith",
        "Regent College London / University of Greater Manchester",
        "March 2026"
      ]
    }
  },
  {
    type: "structure",
    heading: "Presentation Structure",
    items: [
      "Introduction and Study Context",
      "Background: AI in UK Retail Banking",
      "Background: NatWest's Cora",
      "Statement of the Problem",
      "Research Questions",
      "Research Aim and Objectives",
      "Rationale of the Research",
      "Summary of Key Literature",
      "Conceptual Framework",
      "Proposed Methodology",
      "Limitations of the Professional Project",
      "Expected Outcomes",
      "References"
    ]
  },
  {
    type: "content",
    heading: "Introduction and Study Context",
    section: "INTRODUCTION",
    bullets: [
      "The UK banking sector is undergoing significant digital transformation, with artificial intelligence (AI) at its centre. As of 2024, the vast majority of UK adults use online or mobile banking, with digital interactions now dominating the banking landscape.",
      "AI-powered chatbots have become a primary customer service channel for UK retail banks, deployed to offer 24/7 support, reduce costs, and manage growing customer interaction volumes (Wirtz et al., 2018).",
      "Scholars have highlighted that generative AI presents significant opportunities for banking productivity and customer engagement, while also raising concerns around trust, privacy, and ethical deployment (Dwivedi et al., 2023).",
      "Customer satisfaction with these AI tools, however, remains under-researched in the UK context, presenting a timely and contemporary area for academic inquiry.",
      "This study investigates customer satisfaction with NatWest's AI chatbot, Cora, as a case study within UK retail banking."
    ]
  },
  {
    type: "content",
    heading: "Background: AI Chatbots in UK Retail Banking",
    section: "BACKGROUND",
    bullets: [
      "The global AI market in banking has grown rapidly, with the chatbot segment experiencing significant year-on-year growth, reflecting the scale of investment across the sector.",
      "The Bank of England's 2024 AI survey found that 55% of all AI use cases in UK financial services have some degree of automated decision-making (Bank of England, 2024).",
      "UK financial institutions are increasingly reporting productivity gains from AI, with major banks investing heavily in generative AI pilots across customer service, fraud detection, and compliance.",
      "Academic research confirms that while AI chatbots can reduce costs and improve response times, customer acceptance hinges on perceived usefulness, trust, and service quality (Gansser and Reich, 2021). Yet most existing studies focus on markets in Asia, the Middle East, or the USA — very few address the UK retail banking context specifically (Qureshi, Wilkins and Iqbal, 2024)."
    ]
  },
  {
    type: "twocol",
    heading: "Background: NatWest's Cora",
    section: "BACKGROUND",
    left: [
      { label: "Launched", value: "2017 — UK's first banking chatbot" },
      { label: "Initial Scale", value: "1,000 chats/month on 25 topics" },
      { label: "2023 Volume", value: "10.8 million queries (up from 5M in 2019)" },
      { label: "Customers", value: "~19 million across UK" },
      { label: "Channels", value: "Website, Mobile App, WhatsApp" }
    ],
    right: [
      { label: "Cora+ (June 2024)", value: "Generative AI upgrade with IBM — one of the first UK banks to deploy Gen AI through a digital assistant" },
      { label: "AI Partnerships", value: "NatWest has expanded AI partnerships to integrate large language models into Cora" },
      { label: "Resolution Rate", value: "Significant proportion of conversations resolved without human intervention" }
    ],
    refs: "(IBM, 2024; NatWest Group, 2024)"
  },
  {
    type: "problem",
    heading: "Statement of the Problem",
    section: "PROBLEM STATEMENT",
    bankSide: {
      title: "What NatWest Reports",
      color: "#2e7d32",
      items: [
        "150% increase in customer satisfaction since Cora+ launch (IBM, 2024)",
        "Halving in cases requiring colleague intervention",
        "Millions of conversations handled annually"
      ]
    },
    customerSide: {
      title: "What Customers Experience",
      color: "#c62828",
      items: [
        "\"Unable to answer simple questions\" — trapped in repetitive loops (Smart Money People, 2026)",
        "Multi-hour waits for human agent escalation (Trustpilot, 2025)",
        "Basic tasks like ordering replacement cards remain unresolved"
      ]
    },
    gap: "This gap between bank-reported metrics and actual customer experience represents a significant and under-explored research problem."
  },
  {
    type: "content",
    heading: "Statement of the Problem (cont.)",
    section: "PROBLEM STATEMENT",
    bullets: [
      "The problem is compounded by NatWest's increasing strategy of channelling customer interactions through Cora, with reduced access to branch and telephone support.",
      "Trust is a critical factor in financial services, yet chatbots introduce new uncertainties: response accuracy, data handling, and the perceived inability to access human support when needed (Apau, Titis and Lallie, 2025).",
      "In financial services, hallucination risks and inaccurate chatbot responses create specific trust concerns, as demonstrated by widely publicised incidents in the airline and delivery industries where chatbots fabricated policies or used inappropriate language.",
      "Existing academic studies on chatbot satisfaction in banking predominantly focus on non-UK markets, leaving a clear geographical and contextual gap in the literature.",
    ],
    highlight: "In summary: There is a demonstrable gap between how banks measure chatbot success and how customers experience it, particularly in the UK. This study addresses that gap."
  },
  {
    type: "rq",
    heading: "Research Questions",
    section: "RESEARCH QUESTIONS",
    questions: [
      { id: "RQ1", text: "How do NatWest customers perceive the service quality of the AI-powered chatbot Cora in terms of usefulness and ease of use?" },
      { id: "RQ2", text: "To what extent does trust influence customer satisfaction when interacting with AI chatbots in retail banking?" },
      { id: "RQ3", text: "What are the key barriers preventing customers from being satisfied with AI chatbot interactions at NatWest?" }
    ]
  },
  {
    type: "aim",
    heading: "Research Aim",
    section: "RESEARCH AIM",
    aim: "To critically investigate the factors that influence customer satisfaction with AI-powered chatbot technology in UK retail banking, using NatWest's Cora as a case study, and to identify the gap between bank-reported satisfaction metrics and actual customer experience.",
    connection: "This aim directly addresses the problem statement: NatWest claims significant satisfaction improvements, yet independent evidence suggests a contrasting reality. The aim seeks to examine why this gap exists and what drives or hinders customer satisfaction."
  },
  {
    type: "objectives",
    heading: "Research Objectives",
    section: "RESEARCH OBJECTIVES",
    objectives: [
      { id: "O1", text: "To review and critically evaluate existing literature on AI chatbot adoption and customer satisfaction in the banking sector, with particular focus on TAM and UTAUT2.", link: "Builds the theoretical foundation to understand the satisfaction gap identified in the problem" },
      { id: "O2", text: "To examine NatWest customers' perceptions of Cora's service quality, including perceived usefulness, ease of use, and trust.", link: "Directly investigates the customer-side experience underlying the reported satisfaction discrepancy" },
      { id: "O3", text: "To identify the key barriers and drivers of customer satisfaction with AI chatbot interactions at NatWest.", link: "Explains why independent review data contradicts NatWest's internal metrics" },
      { id: "O4", text: "To provide evidence-based recommendations for NatWest and UK retail banks on how to improve customer satisfaction through AI chatbot enhancement.", link: "Translates findings into actionable solutions addressing the identified problems" }
    ]
  },
  {
    type: "rationale",
    heading: "Rationale of the Research",
    section: "RATIONALE",
    items: [
      { type: "Academic", text: "Limited academic research exists on AI chatbot customer satisfaction specifically within UK retail banking. Most existing studies focus on markets in Asia, the Middle East, or the USA (Alshibly et al., 2024; Qureshi, Wilkins and Iqbal, 2024). This study fills a geographical and contextual gap." },
      { type: "Practical", text: "NatWest has invested significantly in AI across its operations, with Cora at the centre of its customer service strategy. As UK banks scale AI chatbot deployment, understanding what drives or hinders customer satisfaction is critical for retention and competitive advantage." },
      { type: "Methodological", text: "The notable discrepancy between NatWest's reported 150% satisfaction improvement and negative independent reviews creates a unique opportunity to examine how satisfaction is measured and experienced differently." },
      { type: "Theoretical", text: "The study extends established frameworks (TAM, UTAUT2) by integrating trust and service quality constructs in the under-studied context of UK banking chatbots, contributing to theoretical development." }
    ]
  },
  {
    type: "lit1",
    heading: "Summary of Literature: Technology Acceptance Frameworks",
    section: "LITERATURE REVIEW",
    frameworks: [
      { name: "TAM", author: "Davis (1989)", desc: "Perceived usefulness (PU) and perceived ease of use (PEOU) are the two primary determinants of technology adoption. Widely applied in chatbot research.", critique: "Criticised for simplicity and limited consideration of contextual factors such as trust and risk (Legris, Ingham and Collerette, 2003)." },
      { name: "UTAUT2", author: "Venkatesh, Thong and Xu (2012)", desc: "Extended UTAUT to consumer contexts, adding hedonic motivation, price value, and habit. Explains 74% of variance in behavioural intention.", critique: "Does not explicitly incorporate trust or security — critical in high-risk banking contexts (Apau, Titis and Lallie, 2025)." }
    ],
    conclusion: "Recent studies have incorporated trust and satisfaction constructs into TAM and UTAUT, recognising that these models alone do not fully capture user experience in sensitive contexts like banking (Venkatesh et al., 2003). This creates the theoretical basis for this study's extended framework."
  },
  {
    type: "content",
    heading: "Summary of Literature: AI Chatbots & Satisfaction in Banking",
    section: "LITERATURE REVIEW",
    bullets: [
      "Qureshi, Wilkins and Iqbal (2024) investigated chatbot service quality and customer satisfaction in banking through qualitative research, identifying eleven themes across three dimensions: perceived service quality, satisfaction, and customer responses/intentions. However, their study used a small sample (n=25) and was not UK-specific.",
      "Alshibly et al. (2024) found that reliability and personalisation significantly predicted customer satisfaction with banking chatbots, both directly and indirectly through customer empowerment. However, other dimensions such as responsiveness were not found to be significant, demonstrating that the relationship between service quality and satisfaction is not uniform across all dimensions.",
      "These mixed findings highlight the context-dependent nature of chatbot satisfaction in banking. What drives satisfaction in one market may not apply in another, underscoring the need for UK-specific research.",
      "The E-S-QUAL framework (Parasuraman, Zeithaml and Malhotra, 2005) provides established dimensions for evaluating electronic service quality — efficiency, fulfilment, system availability, and privacy — applicable to chatbot evaluation in banking."
    ]
  },
  {
    type: "content",
    heading: "Summary of Literature: Trust in AI Banking",
    section: "LITERATURE REVIEW",
    bullets: [
      "Trust is consistently identified as a critical mediator between technology adoption and satisfaction in financial services, where customers share sensitive personal and financial data (Apau, Titis and Lallie, 2025).",
      "Apau, Titis and Lallie (2025) expanded UTAUT2 with security, risk, institutional trust, and technology trust in the mobile banking context, with the model explaining 79% of variance in behavioural intention. This demonstrates the significant explanatory power trust adds to standard acceptance models.",
      "Wirtz et al. (2018) proposed the Service Robot Acceptance Model (sRAM), highlighting that customer willingness to engage with AI-driven service agents depends on functional, socio-emotional, and relational factors including trust.",
      "The literature therefore strongly supports incorporating trust as a key construct alongside perceived usefulness, ease of use, and service quality in the proposed conceptual framework for this study."
    ]
  },
  {
    type: "framework",
    heading: "Conceptual Framework",
    section: "CONCEPTUAL FRAMEWORK"
  },
  {
    type: "methodology",
    heading: "Proposed Methodology: Philosophy, Approach & Strategy",
    section: "METHODOLOGY",
    rows: [
      { label: "Research Philosophy", value: "Pragmatism", desc: "Focuses on practical outcomes; allows multiple methods to answer research questions (Saunders, Lewis and Thornhill, 2019)" },
      { label: "Research Approach", value: "Deductive with inductive elements", desc: "Tests relationships from the conceptual framework; allows new themes to emerge from qualitative data (Creswell and Creswell, 2018)" },
      { label: "Methodological Choice", value: "Mixed Methods", desc: "Convergent parallel design — quantitative and qualitative data collected concurrently (Creswell and Creswell, 2018)" },
      { label: "Research Strategy", value: "Survey", desc: "" },
      { label: "Time Horizon", value: "Cross-sectional", desc: "" }
    ]
  },
  {
    type: "datacollection",
    heading: "Proposed Methodology: Data Collection & Sampling",
    section: "METHODOLOGY",
    primary: [
      "Online questionnaire distributed to NatWest customers who have used Cora",
      "Likert-scale items adapted from validated TAM, UTAUT2, and E-S-QUAL instruments",
      "Open-ended qualitative questions on barriers and experiences"
    ],
    secondary: [
      "Analysis of publicly available customer reviews (Trustpilot, Smart Money People)",
      "NatWest's published Cora performance data"
    ],
    sampling: "Non-probability purposive and snowball sampling — targeting NatWest customers with direct Cora experience",
    sampleSize: "Minimum 100 survey respondents",
    distribution: "Online via social media, banking forums, and relevant communities"
  },
  {
    type: "analysis",
    heading: "Proposed Methodology: Data Analysis & Ethics",
    section: "METHODOLOGY",
    quant: "SPSS — descriptive statistics, correlation analysis, and multiple regression to test relationships in the conceptual framework",
    qual: "Thematic analysis following the six-phase approach of Braun and Clarke (2006) to identify recurring patterns in open-ended responses",
    ethics: [
      "Informed consent from all participants",
      "Anonymity and confidentiality ensured",
      "Compliance with UK Data Protection Act 2018 and GDPR",
      "University ethics approval via RE1 form",
      "Right to withdraw at any stage without penalty"
    ]
  },
  {
    type: "onion",
    heading: "Research Onion Summary",
    section: "METHODOLOGY",
    layers: [
      { layer: "Philosophy", choice: "Pragmatism" },
      { layer: "Approach", choice: "Deductive (with inductive elements)" },
      { layer: "Methodological Choice", choice: "Mixed Methods" },
      { layer: "Strategy", choice: "Survey" },
      { layer: "Time Horizon", choice: "Cross-sectional" },
      { layer: "Sampling", choice: "Purposive and Snowball" },
      { layer: "Data Collection", choice: "Online Questionnaire + Secondary Review Data" },
      { layer: "Data Analysis", choice: "SPSS + Thematic Analysis" },
      { layer: "Ethics", choice: "RE1 form, GDPR compliance, informed consent" }
    ]
  },
  {
    type: "content",
    heading: "Limitations of the Professional Project",
    section: "LIMITATIONS",
    bullets: [
      "Single case study: Focusing on NatWest's Cora alone may limit transferability of findings to other UK banks or chatbot implementations.",
      "Geographical scope: Limited to the UK retail banking context, reducing generalisability to other national banking markets.",
      "Cross-sectional design: Data captured at one point in time; cannot track how satisfaction evolves as Cora continues to be upgraded.",
      "Sampling bias: Non-probability sampling may not fully represent NatWest's 19 million customer base; respondents with strong views may be overrepresented.",
      "Self-reported data: Perceptions are subject to recall bias and social desirability effects.",
      "Rapidly evolving technology: NatWest's AI capabilities are developing quickly, meaning findings may have a limited shelf life as the technology continues to mature."
    ]
  },
  {
    type: "content",
    heading: "Expected Outcomes of the Professional Project",
    section: "EXPECTED OUTCOMES",
    bullets: [
      "Identification of the key factors (perceived usefulness, ease of use, trust, service quality) that most significantly influence customer satisfaction with Cora.",
      "Empirical evidence documenting the gap between NatWest's internally reported Cora metrics and customer experience on independent platforms.",
      "A validated extended conceptual framework combining TAM, UTAUT2 trust constructs, and E-S-QUAL, applicable to UK banking chatbots.",
      "Identification of specific barriers to satisfaction (e.g., complex query handling, escalation failures, loop issues, lack of empathy).",
      "Practical, evidence-based recommendations for NatWest and UK retail banks to improve chatbot design, enhance trust, and strengthen human escalation pathways.",
      "Contribution to the limited body of academic literature on AI chatbot satisfaction in UK retail banking."
    ]
  },
  {
    type: "references",
    heading: "References",
    section: "REFERENCES",
    refs: [
      "Alshibly, H.H., Alwreikat, A., Morgos, R. and Abuaddous, M.Y. (2024) 'Examining the mediating role of customer empowerment: the impact of chatbot usability on customer satisfaction in Jordanian commercial banks', Cogent Business & Management, 11(1), p.2387196.",
      "Apau, R., Titis, E. and Lallie, H.S. (2025) 'Towards a better understanding of mobile banking app adoption and use: Integrating security, risk, and trust into UTAUT2', Computers, 14(4), p.144.",
      "Bank of England (2024) Artificial Intelligence in UK Financial Services – 2024. Available at: https://www.bankofengland.co.uk/report/2024/artificial-intelligence-in-uk-financial-services-2024 (Accessed: 14 March 2026).",
      "Braun, V. and Clarke, V. (2006) 'Using thematic analysis in psychology', Qualitative Research in Psychology, 3(2), pp.77–101.",
      "Creswell, J.W. and Creswell, J.D. (2018) Research Design: Qualitative, Quantitative, and Mixed Methods Approaches. 5th edn. London: SAGE Publications.",
      "Davis, F.D. (1989) 'Perceived usefulness, perceived ease of use, and user acceptance of information technology', MIS Quarterly, 13(3), pp.319–340.",
      "Dwivedi, Y.K., Kshetri, N., Hughes, L., Slade, E.L., Jeyaraj, A., Kar, A.K., Baabdullah, A.M., Koohang, A., Raghavan, V., Ahuja, M. and Albanna, H. (2023) 'Opinion paper: \"So what if ChatGPT wrote it?\"', International Journal of Information Management, 71, p.102642.",
      "Gansser, O.A. and Reich, C.S. (2021) 'A new acceptance model for artificial intelligence with extensions to UTAUT2', Technology in Society, 65, p.101535.",
      "IBM (2024) NatWest: AI-led answers, empathy-led service. Available at: https://www.ibm.com/case-studies/natwest (Accessed: 14 March 2026).",
      "Legris, P., Ingham, J. and Collerette, P. (2003) 'Why do people use information technology? A critical review of the technology acceptance model', Information & Management, 40(3), pp.191–204.",
      "NatWest Group (2024) NatWest launches Cora+, the latest generative AI upgrade to the bank's digital assistant. Available at: https://www.natwestgroup.com (Accessed: 14 March 2026).",
      "Parasuraman, A., Zeithaml, V.A. and Malhotra, A. (2005) 'E-S-QUAL: A multiple-item scale for assessing electronic service quality', Journal of Service Research, 7(3), pp.213–233.",
      "Qureshi, O.A., Wilkins, S. and Iqbal, H. (2024) 'Chatbots: Can they satisfy customers in the banking sector?', in Al Marri, K. et al. (eds.) BUiD Doctoral Research Conference 2023. LNCE, vol. 473. Cham: Springer.",
      "Saunders, M., Lewis, P. and Thornhill, A. (2019) Research Methods for Business Students. 8th edn. Harlow: Pearson Education.",
      "Smart Money People (2026) NatWest Group – Cora Digital Assistant Reviews. Available at: https://smartmoneypeople.com (Accessed: 14 March 2026).",
      "Trustpilot (2025) NatWest Reviews. Available at: https://www.trustpilot.com/review/www.natwest.com (Accessed: 14 March 2026).",
      "Venkatesh, V., Morris, M.G., Davis, G.B. and Davis, F.D. (2003) 'User acceptance of information technology: Toward a unified view', MIS Quarterly, 27(3), pp.425–478.",
      "Venkatesh, V., Thong, J.Y. and Xu, X. (2012) 'Consumer acceptance and use of information technology: Extending the unified theory of acceptance and use of technology', MIS Quarterly, 36(1), pp.157–178.",
      "Wirtz, J., Patterson, P.G., Kunz, W.H., Gruber, T., Lu, V.N., Paluch, S. and Martins, A. (2018) 'Brave new world: service robots in the frontline', Journal of Service Management, 29(5), pp.907–931."
    ]
  }
];

const navy = "#1a2744";
const accent = "#2c5282";
const lightBg = "#f7f8fa";
const green = "#2e7d32";
const red = "#c62828";

function SlideTitle({ s }) {
  return (
    <div style={{ display:"flex", flexDirection:"column", justifyContent:"center", alignItems:"center", height:"100%", textAlign:"center", padding:"40px" }}>
      <div style={{ fontSize:"11px", letterSpacing:"3px", color:accent, marginBottom:"20px", fontWeight:600 }}>MBA7067 – PROFESSIONAL PROJECT</div>
      <h1 style={{ fontSize:"26px", color:navy, fontWeight:700, lineHeight:1.3, marginBottom:"8px", maxWidth:"90%" }}>{s.content.title}</h1>
      <h2 style={{ fontSize:"18px", color:accent, fontWeight:500, marginBottom:"30px" }}>{s.content.subtitle}</h2>
      <div style={{ borderTop:`2px solid ${accent}`, width:"80px", marginBottom:"20px" }}></div>
      {s.content.meta.map((m,i) => <div key={i} style={{ fontSize:"12px", color:"#555", marginBottom:"4px" }}>{m}</div>)}
    </div>
  );
}

function SlideStructure({ s }) {
  return (
    <div style={{ padding:"30px 40px" }}>
      <SectionLabel text="OVERVIEW" />
      <H>{s.heading}</H>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"8px", marginTop:"16px" }}>
        {s.items.map((it,i) => (
          <div key={i} style={{ display:"flex", alignItems:"center", gap:"10px", padding:"8px 12px", background:i%2===0?"#eef2f7":"#f5f7fa", borderRadius:"6px", fontSize:"12px", color:"#333" }}>
            <span style={{ background:accent, color:"#fff", borderRadius:"50%", width:"22px", height:"22px", display:"flex", alignItems:"center", justifyContent:"center", fontSize:"10px", fontWeight:700, flexShrink:0 }}>{i+1}</span>
            {it}
          </div>
        ))}
      </div>
    </div>
  );
}

function SlideContent({ s }) {
  return (
    <div style={{ padding:"30px 40px" }}>
      {s.section && <SectionLabel text={s.section} />}
      <H>{s.heading}</H>
      <div style={{ marginTop:"14px" }}>
        {s.bullets.map((b,i) => <Bullet key={i} text={b} />)}
      </div>
      {s.highlight && <div style={{ marginTop:"14px", padding:"12px 16px", background:"#e8edf4", borderLeft:`4px solid ${accent}`, borderRadius:"4px", fontSize:"12px", fontWeight:600, color:navy }}>{s.highlight}</div>}
    </div>
  );
}

function SlideProblem({ s }) {
  return (
    <div style={{ padding:"30px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"16px", marginTop:"14px" }}>
        <div style={{ background:"#e8f5e9", borderRadius:"8px", padding:"14px", borderTop:`4px solid ${green}` }}>
          <div style={{ fontSize:"13px", fontWeight:700, color:green, marginBottom:"8px" }}>{s.bankSide.title}</div>
          {s.bankSide.items.map((it,i) => <div key={i} style={{ fontSize:"11px", color:"#333", marginBottom:"6px", paddingLeft:"12px", borderLeft:`2px solid ${green}` }}>{it}</div>)}
        </div>
        <div style={{ background:"#fbe9e7", borderRadius:"8px", padding:"14px", borderTop:`4px solid ${red}` }}>
          <div style={{ fontSize:"13px", fontWeight:700, color:red, marginBottom:"8px" }}>{s.customerSide.title}</div>
          {s.customerSide.items.map((it,i) => <div key={i} style={{ fontSize:"11px", color:"#333", marginBottom:"6px", paddingLeft:"12px", borderLeft:`2px solid ${red}` }}>{it}</div>)}
        </div>
      </div>
      <div style={{ marginTop:"14px", padding:"10px 14px", background:"#fff3e0", borderLeft:`4px solid #e65100`, borderRadius:"4px", fontSize:"12px", fontWeight:600, color:"#bf360c" }}>⚠ {s.gap}</div>
    </div>
  );
}

function SlideRQ({ s }) {
  return (
    <div style={{ padding:"30px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ marginTop:"16px", display:"flex", flexDirection:"column", gap:"14px" }}>
        {s.questions.map((q,i) => (
          <div key={i} style={{ display:"flex", gap:"14px", alignItems:"flex-start", padding:"14px 16px", background:lightBg, borderRadius:"8px", borderLeft:`4px solid ${accent}` }}>
            <span style={{ background:accent, color:"#fff", padding:"4px 10px", borderRadius:"4px", fontSize:"13px", fontWeight:700, flexShrink:0 }}>{q.id}</span>
            <span style={{ fontSize:"13px", color:"#333", lineHeight:1.5 }}>{q.text}</span>
          </div>
        ))}
      </div>
    </div>
  );
}

function SlideAim({ s }) {
  return (
    <div style={{ padding:"30px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ marginTop:"16px", padding:"18px 20px", background:lightBg, borderLeft:`4px solid ${accent}`, borderRadius:"8px" }}>
        <div style={{ fontSize:"11px", fontWeight:700, color:accent, marginBottom:"6px" }}>AIM</div>
        <div style={{ fontSize:"13px", color:"#333", lineHeight:1.6 }}>{s.aim}</div>
      </div>
      <div style={{ marginTop:"14px", padding:"14px 16px", background:"#fff", border:"1px solid #e0e0e0", borderRadius:"8px", fontSize:"12px", color:"#555", lineHeight:1.5 }}>{s.connection}</div>
    </div>
  );
}

function SlideObjectives({ s }) {
  return (
    <div style={{ padding:"28px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ marginTop:"12px", display:"flex", flexDirection:"column", gap:"10px" }}>
        {s.objectives.map((o,i) => (
          <div key={i} style={{ display:"flex", gap:"12px", alignItems:"flex-start", padding:"10px 14px", background:lightBg, borderRadius:"8px", borderLeft:`4px solid ${accent}` }}>
            <span style={{ background:navy, color:"#fff", padding:"3px 8px", borderRadius:"4px", fontSize:"12px", fontWeight:700, flexShrink:0 }}>{o.id}</span>
            <div>
              <div style={{ fontSize:"12px", color:"#333", lineHeight:1.5 }}>{o.text}</div>
              <div style={{ fontSize:"10px", color:accent, fontStyle:"italic", marginTop:"3px" }}>→ {o.link}</div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

function SlideRationale({ s }) {
  const icons = { Academic:"📚", Practical:"💼", Methodological:"🔬", Theoretical:"🧠" };
  return (
    <div style={{ padding:"30px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ marginTop:"14px", display:"grid", gridTemplateColumns:"1fr 1fr", gap:"12px" }}>
        {s.items.map((it,i) => (
          <div key={i} style={{ padding:"12px 14px", background:lightBg, borderRadius:"8px", borderTop:`3px solid ${accent}` }}>
            <div style={{ fontSize:"12px", fontWeight:700, color:accent, marginBottom:"6px" }}>{icons[it.type]} {it.type} Rationale</div>
            <div style={{ fontSize:"11px", color:"#333", lineHeight:1.5 }}>{it.text}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function SlideLit1({ s }) {
  return (
    <div style={{ padding:"28px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ marginTop:"12px", display:"flex", flexDirection:"column", gap:"12px" }}>
        {s.frameworks.map((f,i) => (
          <div key={i} style={{ display:"grid", gridTemplateColumns:"80px 1fr", gap:"12px", padding:"12px", background:lightBg, borderRadius:"8px", borderLeft:`4px solid ${accent}` }}>
            <div style={{ display:"flex", flexDirection:"column", justifyContent:"center", alignItems:"center" }}>
              <div style={{ fontSize:"16px", fontWeight:800, color:navy }}>{f.name}</div>
              <div style={{ fontSize:"9px", color:"#666", textAlign:"center", marginTop:"2px" }}>{f.author}</div>
            </div>
            <div>
              <div style={{ fontSize:"11px", color:"#333", lineHeight:1.5, marginBottom:"4px" }}>{f.desc}</div>
              <div style={{ fontSize:"10px", color:red, fontStyle:"italic" }}>Limitation: {f.critique}</div>
            </div>
          </div>
        ))}
      </div>
      <div style={{ marginTop:"10px", padding:"10px 14px", background:"#e8edf4", borderRadius:"6px", fontSize:"11px", color:"#333", lineHeight:1.5 }}>{s.conclusion}</div>
    </div>
  );
}

function SlideTwoCol({ s }) {
  return (
    <div style={{ padding:"30px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"16px", marginTop:"14px" }}>
        <div style={{ background:lightBg, borderRadius:"8px", padding:"14px", borderTop:`3px solid ${navy}` }}>
          <div style={{ fontSize:"12px", fontWeight:700, color:navy, marginBottom:"10px" }}>Key Facts</div>
          {s.left.map((it,i) => <div key={i} style={{ marginBottom:"8px" }}><span style={{ fontSize:"10px", fontWeight:700, color:accent }}>{it.label}: </span><span style={{ fontSize:"11px", color:"#333" }}>{it.value}</span></div>)}
        </div>
        <div style={{ background:lightBg, borderRadius:"8px", padding:"14px", borderTop:`3px solid ${accent}` }}>
          <div style={{ fontSize:"12px", fontWeight:700, color:accent, marginBottom:"10px" }}>Recent Developments</div>
          {s.right.map((it,i) => <div key={i} style={{ marginBottom:"8px" }}><span style={{ fontSize:"10px", fontWeight:700, color:accent }}>{it.label}: </span><span style={{ fontSize:"11px", color:"#333" }}>{it.value}</span></div>)}
        </div>
      </div>
      <div style={{ marginTop:"8px", fontSize:"10px", color:"#888", textAlign:"right" }}>{s.refs}</div>
    </div>
  );
}

function SlideFramework() {
  const bx = (label, bg, border, w) => ({ padding:"8px 10px", background:bg, border:`2px solid ${border}`, borderRadius:"6px", fontSize:"10px", fontWeight:600, color:navy, textAlign:"center", width:w||"auto" });
  return (
    <div style={{ padding:"28px 40px" }}>
      <SectionLabel text="CONCEPTUAL FRAMEWORK" />
      <H>Conceptual Framework</H>
      <div style={{ fontSize:"10px", color:"#666", marginBottom:"10px" }}>Theoretical Foundation: Extended TAM + UTAUT2 Trust Constructs + E-S-QUAL</div>
      <div style={{ display:"flex", gap:"16px", alignItems:"center", justifyContent:"center", flexWrap:"wrap" }}>
        <div style={{ display:"flex", flexDirection:"column", gap:"8px" }}>
          <div style={bx("", "#e3f2fd", "#2196f3")}>Perceived Usefulness<br/><span style={{fontSize:"8px",fontWeight:400}}>(Davis, 1989)</span></div>
          <div style={bx("", "#e3f2fd", "#2196f3")}>Perceived Ease of Use<br/><span style={{fontSize:"8px",fontWeight:400}}>(Davis, 1989)</span></div>
          <div style={bx("", "#e8f5e9", "#4caf50")}>Trust: Institutional &<br/>Technology Trust<br/><span style={{fontSize:"8px",fontWeight:400}}>(Apau et al., 2025)</span></div>
          <div style={bx("", "#fff3e0", "#ff9800")}>Service Quality:<br/>Reliability, Personalisation<br/><span style={{fontSize:"8px",fontWeight:400}}>(Parasuraman et al., 2005)</span></div>
        </div>
        <div style={{ display:"flex", flexDirection:"column", alignItems:"center", gap:"4px" }}>
          <div style={{ fontSize:"18px", color:accent }}>→</div>
          <div style={{ fontSize:"18px", color:accent }}>→</div>
          <div style={{ fontSize:"18px", color:accent }}>→</div>
          <div style={{ fontSize:"18px", color:accent }}>→</div>
        </div>
        <div style={{ display:"flex", flexDirection:"column", gap:"10px", alignItems:"center" }}>
          <div style={{ ...bx("", "#e8eaf6", navy), padding:"16px 20px", fontSize:"13px", fontWeight:700 }}>Customer<br/>Satisfaction</div>
          <div style={{ fontSize:"14px", color:accent }}>↓</div>
          <div style={bx("", "#f3e5f5", "#7b1fa2")}>Continuance<br/>Intention</div>
        </div>
      </div>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"10px", marginTop:"12px" }}>
        <div style={{ background:"#fbe9e7", padding:"8px 10px", borderRadius:"6px" }}>
          <div style={{ fontSize:"10px", fontWeight:700, color:red, marginBottom:"4px" }}>Barriers (RQ3)</div>
          <div style={{ fontSize:"9px", color:"#333", lineHeight:1.5 }}>• Complex query handling • Escalation difficulty • Privacy concerns • Lack of empathy</div>
        </div>
        <div style={{ background:"#f5f5f5", padding:"8px 10px", borderRadius:"6px" }}>
          <div style={{ fontSize:"10px", fontWeight:700, color:"#555", marginBottom:"4px" }}>Moderating Variables</div>
          <div style={{ fontSize:"9px", color:"#333", lineHeight:1.5 }}>• Customer demographics (age, digital literacy) • Complexity of banking query</div>
        </div>
      </div>
    </div>
  );
}

function SlideMethodology({ s }) {
  return (
    <div style={{ padding:"28px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ marginTop:"12px" }}>
        {s.rows.map((r,i) => (
          <div key={i} style={{ display:"grid", gridTemplateColumns:"160px 160px 1fr", gap:"8px", padding:"8px 0", borderBottom:"1px solid #eee", alignItems:"center" }}>
            <div style={{ fontSize:"11px", fontWeight:700, color:navy }}>{r.label}</div>
            <div style={{ fontSize:"11px", fontWeight:600, color:accent, background:"#eef2f7", padding:"4px 8px", borderRadius:"4px", textAlign:"center" }}>{r.value}</div>
            <div style={{ fontSize:"10px", color:"#555" }}>{r.desc}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

function SlideDataCollection({ s }) {
  return (
    <div style={{ padding:"28px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"14px", marginTop:"12px" }}>
        <div style={{ background:lightBg, padding:"12px", borderRadius:"8px", borderTop:`3px solid ${navy}` }}>
          <div style={{ fontSize:"11px", fontWeight:700, color:navy, marginBottom:"8px" }}>Primary Data</div>
          {s.primary.map((p,i) => <div key={i} style={{ fontSize:"10px", color:"#333", marginBottom:"4px", paddingLeft:"8px", borderLeft:`2px solid ${accent}` }}>{p}</div>)}
        </div>
        <div style={{ background:lightBg, padding:"12px", borderRadius:"8px", borderTop:`3px solid ${accent}` }}>
          <div style={{ fontSize:"11px", fontWeight:700, color:accent, marginBottom:"8px" }}>Secondary Data</div>
          {s.secondary.map((p,i) => <div key={i} style={{ fontSize:"10px", color:"#333", marginBottom:"4px", paddingLeft:"8px", borderLeft:`2px solid ${accent}` }}>{p}</div>)}
        </div>
      </div>
      <div style={{ marginTop:"10px", display:"grid", gridTemplateColumns:"1fr 1fr 1fr", gap:"8px" }}>
        <div style={{ background:"#e8edf4", padding:"8px", borderRadius:"6px", fontSize:"10px" }}><strong>Sampling:</strong> {s.sampling}</div>
        <div style={{ background:"#e8edf4", padding:"8px", borderRadius:"6px", fontSize:"10px" }}><strong>Sample Size:</strong> {s.sampleSize}</div>
        <div style={{ background:"#e8edf4", padding:"8px", borderRadius:"6px", fontSize:"10px" }}><strong>Distribution:</strong> {s.distribution}</div>
      </div>
    </div>
  );
}

function SlideAnalysis({ s }) {
  return (
    <div style={{ padding:"28px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"14px", marginTop:"14px" }}>
        <div style={{ background:"#e3f2fd", padding:"14px", borderRadius:"8px" }}>
          <div style={{ fontSize:"11px", fontWeight:700, color:navy, marginBottom:"6px" }}>📊 Quantitative Analysis</div>
          <div style={{ fontSize:"11px", color:"#333", lineHeight:1.5 }}>{s.quant}</div>
        </div>
        <div style={{ background:"#e8f5e9", padding:"14px", borderRadius:"8px" }}>
          <div style={{ fontSize:"11px", fontWeight:700, color:green, marginBottom:"6px" }}>📝 Qualitative Analysis</div>
          <div style={{ fontSize:"11px", color:"#333", lineHeight:1.5 }}>{s.qual}</div>
        </div>
      </div>
      <div style={{ marginTop:"14px", background:lightBg, padding:"14px", borderRadius:"8px", borderTop:`3px solid ${accent}` }}>
        <div style={{ fontSize:"11px", fontWeight:700, color:accent, marginBottom:"8px" }}>🔒 Ethical Considerations</div>
        <div style={{ display:"grid", gridTemplateColumns:"1fr 1fr", gap:"4px" }}>
          {s.ethics.map((e,i) => <div key={i} style={{ fontSize:"10px", color:"#333", paddingLeft:"8px", borderLeft:`2px solid ${accent}` }}>{e}</div>)}
        </div>
      </div>
    </div>
  );
}

function SlideOnion({ s }) {
  return (
    <div style={{ padding:"28px 40px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ fontSize:"10px", color:"#666", marginBottom:"10px" }}>Adapted from Saunders, Lewis and Thornhill (2019)</div>
      <div style={{ display:"flex", flexDirection:"column", alignItems:"center", gap:"4px" }}>
        {s.layers.map((l,i) => {
          const w = 95 - i*5;
          const op = 0.15 + i*0.05;
          return (
            <div key={i} style={{ width:`${w}%`, display:"grid", gridTemplateColumns:"1fr 1fr", background:`rgba(44,82,130,${op})`, padding:"8px 14px", borderRadius:"20px", alignItems:"center" }}>
              <div style={{ fontSize:"11px", fontWeight:700, color:navy, textAlign:"right", paddingRight:"12px" }}>{l.layer}</div>
              <div style={{ fontSize:"11px", color:"#333", textAlign:"left", paddingLeft:"12px", borderLeft:`2px solid ${accent}` }}>{l.choice}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
}

function SlideRefs({ s }) {
  return (
    <div style={{ padding:"24px 36px" }}>
      <SectionLabel text={s.section} />
      <H>{s.heading}</H>
      <div style={{ marginTop:"10px", maxHeight:"380px", overflowY:"auto", paddingRight:"8px" }}>
        {s.refs.map((r,i) => (
          <div key={i} style={{ fontSize:"9.5px", color:"#333", lineHeight:1.5, marginBottom:"6px", paddingLeft:"10px", borderLeft:`2px solid ${accent}`, background:i%2===0?"#fafbfc":"#fff", padding:"4px 8px 4px 10px", borderRadius:"3px" }}>{r}</div>
        ))}
      </div>
    </div>
  );
}

function SectionLabel({ text }) {
  return <div style={{ fontSize:"9px", letterSpacing:"2px", color:accent, fontWeight:700, marginBottom:"6px" }}>{text}</div>;
}

function H({ children }) {
  return <h2 style={{ fontSize:"20px", color:navy, fontWeight:700, marginBottom:"4px", paddingBottom:"8px", borderBottom:`2px solid ${accent}` }}>{children}</h2>;
}

function Bullet({ text }) {
  return (
    <div style={{ display:"flex", gap:"10px", alignItems:"flex-start", marginBottom:"10px" }}>
      <span style={{ marginTop:"5px", width:"6px", height:"6px", borderRadius:"50%", background:accent, flexShrink:0 }}></span>
      <span style={{ fontSize:"12px", color:"#333", lineHeight:1.6 }}>{text}</span>
    </div>
  );
}

const renderers = {
  title: SlideTitle, structure: SlideStructure, content: SlideContent, problem: SlideProblem,
  rq: SlideRQ, aim: SlideAim, objectives: SlideObjectives, rationale: SlideRationale,
  lit1: SlideLit1, twocol: SlideTwoCol, framework: SlideFramework, methodology: SlideMethodology,
  datacollection: SlideDataCollection, analysis: SlideAnalysis, onion: SlideOnion, references: SlideRefs
};

export default function App() {
  const [cur, setCur] = useState(0);
  const s = slides[cur];
  const Renderer = renderers[s.type] || SlideContent;

  return (
    <div style={{ fontFamily:"'Segoe UI','Helvetica Neue',Arial,sans-serif", maxWidth:"820px", margin:"0 auto" }}>
      <div style={{ background:"#fff", borderRadius:"8px", boxShadow:"0 2px 20px rgba(0,0,0,0.12)", overflow:"hidden", aspectRatio:"16/10", position:"relative", border:"1px solid #e0e0e0" }}>
        <div style={{ position:"absolute", top:0, left:0, right:0, height:"3px", background:`linear-gradient(90deg, ${navy}, ${accent})` }}></div>
        <div style={{ height:"100%", overflowY:"auto" }}>
          <Renderer s={s} />
        </div>
        <div style={{ position:"absolute", bottom:"8px", right:"16px", fontSize:"10px", color:"#aaa" }}>
          {cur+1} / {slides.length}
        </div>
      </div>
      <div style={{ display:"flex", justifyContent:"space-between", alignItems:"center", marginTop:"12px", padding:"0 4px" }}>
        <button onClick={() => setCur(Math.max(0,cur-1))} disabled={cur===0} style={{ padding:"8px 20px", background:cur===0?"#ccc":navy, color:"#fff", border:"none", borderRadius:"6px", cursor:cur===0?"default":"pointer", fontSize:"12px", fontWeight:600 }}>← Previous</button>
        <div style={{ display:"flex", gap:"4px", flexWrap:"wrap", justifyContent:"center", maxWidth:"500px" }}>
          {slides.map((_,i) => (
            <button key={i} onClick={() => setCur(i)} style={{ width:"20px", height:"20px", borderRadius:"4px", border:"none", background:i===cur?accent:"#e0e0e0", color:i===cur?"#fff":"#666", fontSize:"9px", cursor:"pointer", fontWeight:i===cur?700:400 }}>{i+1}</button>
          ))}
        </div>
        <button onClick={() => setCur(Math.min(slides.length-1,cur+1))} disabled={cur===slides.length-1} style={{ padding:"8px 20px", background:cur===slides.length-1?"#ccc":navy, color:"#fff", border:"none", borderRadius:"6px", cursor:cur===slides.length-1?"default":"pointer", fontSize:"12px", fontWeight:600 }}>Next →</button>
      </div>
    </div>
  );
}
