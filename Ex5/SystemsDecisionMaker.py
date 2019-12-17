def systems_decision_maker(graph) -> dict:
    """Inizialmente considero tutti i vertici come se avessero il sistema. 
    full_coverage rappresenta che tutti i vertici a lui adiacenti hanno il sistema.
    full_coverage_degree rappresenta il numero di amici che hanno il parametro full_coverage = true."""
    for v in graph.vertices():
        v.set_system(True)
        v.set_initial_full_coverage(True)
        v.set_full_coverage_degree(graph.degree(v))

    """Effettuo il controllo su tutti i vertici del grafo"""
    for v in graph.vertices():

        """Se il vertice e tutti i suoi amici hanno il sistema, il vertice è uno dei candidati a non avere
         più il sistema"""
        if v.system() & v.full_coverage():

            """Cerco il vertice con full_coverage = true e che abbia il minor numero di amici con full_coverage=true.
            Mi conviene prendere il minore rispetto a full_coverage_degree invece che a degree perchè così riesco a
            raggiungere una soluzione più vicina a quella ottimale (so che questo ragionamento è troppo ingarbugliato,
            per qualsiasi domanda non esitate a chiedere)"""
            min=v
            for e in graph.incident_edges(v):
                u = e.opposite(v)
                if u.full_coverage() and (min.full_coverage_degree() > u.full_coverage_degree()):
                    min=u

            """Rimuovo il sistema dal vertice e setto il parametro full_coverage di tutti i suoi amici a false"""
            min.set_system(False)
            for e in graph.incident_edges(min):
                u = e.opposite(min)
                """in set_full_coverage avviene il decremento del full_coverage_degree dei vicini di u"""
                u.set_full_coverage(False, graph)
    return graph










