o protect a Java XMLInputFactory from XXE, do this:

// This disables DTDs entirely for that factory
xmlInputFactory.setProperty(XMLInputFactory.SUPPORT_DTD, false); 
// disable external entities
xmlInputFactory.setProperty("javax.xml.stream.isSupportingExternalEntities", false); 