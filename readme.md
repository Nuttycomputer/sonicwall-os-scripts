## Sonicwall Scripts

### Quick Start

#### Install depdendencies:

```
pip install -r requirements.txt
```

#### Create `sonicwall_xml.xml` by logging into your sonicwall and running the following:

- no cli pager session

Turn on logging if not already done. (See your ssh client for help turning on logging)

- show access-rules xml

Then prune the file so you only have the xml document and save as 'sonicwall_xml.xml' in script installation directory.