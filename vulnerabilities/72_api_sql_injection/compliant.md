String q='SELECT r FROM  User r where r.userId=''+user+''';
Query query=em.createQuery(q);
List users=query.getResultList();