import myJson from './../neo/login.json' assert {type: 'json'};

let neoViz;

function draw() {
    var config = {
        containerId: "viz",
        neo4j: {
            serverUrl: "bolt://" + myJson["server-ip"] + ":7687",
            serverUser: myJson["neo-user"],
            serverPassword: myJson["neo-pass"]
        },
        visConfig: {
            nodes: {
            },
            edges: {
                arrows: {
                    to: {enabled: true}
                },
                
                font:{color: "white", size:4, strokeWidth: 0},
            },
            groups: {
                univerzita: {color:{border:'#5db665', background:'#8DCC93', highlight: {border: "#5db665", background:"#7bc482"}}, shape:"circle", font:{color: "black", size:8, strokeWidth: 0}, size:6},
                fakulta: {color:{border:'#2870c2', background:'#4C8EDA', highlight: {border: "#2870c2", background:"#3781d6"}}, shape:"circle", font:{color: "black", size:8, strokeWidth: 0}, size:6},
                clovek: {color:{border:'#d7a013', background:'#FFC454', highlight: {border: "#d7a013", background:"#ffbb3b"}}, shape:"dot", font:{color: "black", size:8, strokeWidth: 2}, size:6},
                pracoviste: {color:{border:'#eb2728', background:'#F16667', highlight: {border: "#eb2728", background:"#ef4f50"}}, shape:"circle", font:{color: "white", size:8, strokeWidth: 0}, size:6}
            },
            layout: {
                clusterThreshold: 200
            },
            interaction: {
                navigationButtons: true
            }
        },
        labels: {
            Univerzita: {
                label: "name",
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                        group: "univerzita",
                    }
                }
            },
            Fakulta: {
                label: "name",
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    group: "fakulta"
                    }
                }
            },
            Clovek: {
                label: "name",
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    group: "clovek"
                    }
                }
            },
            Pracoviste: {
                label: "name",
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    group: "pracoviste"
                    }
                }
            }
        },
        relationships:{
            HAS_FAKULTA:{
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    label: "HAS_FAKULTA"
                    }
                }
            },IS_WORKING_AT:{
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    label: "IS_WORKING_AT"
                    }
                }
            },IS_WORKING_IN:{
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    label: "IS_WORKING_IN"
                    }
                }
            },HAS_WORKPLACE:{
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    label: "HAS_WORKPLACE"
                    }
                }
            },IS_WORKING_WITH:{
                [NeoVis.NEOVIS_ADVANCED_CONFIG]: {
                    static: {
                    label: "IS_WORKING_WITH"
                    }
                }
            },
        },
        initialCypher: "MATCH (u:Univerzita)-[hasfak:HAS_FAKULTA]->(f:Fakulta)<-[iswor:IS_WORKING_AT]-(c:Clovek)-[iswork:IS_WORKING_IN]->(p:Pracoviste)<-[haswo:HAS_WORKPLACE]-(f:Fakulta) MATCH (c1:Clovek)-[workwith:IS_WORKING_WITH]->(c2:Clovek) RETURN " + q
    };
    neoViz = new NeoVis.default(config);
    neoViz.render();
}
window.onload = draw()