
from fatcat_client.models import ReleaseEntity

class FatcatRelease(ReleaseEntity):
    """
    This is a wrapper class that extends the code-generated `ReleaseEntity`
    class with extra methods.
    """

    def to_elastic_dict(self):
        """
        Converts from an entity model/schema to elasticsearch oriented schema.

        Returns: dict
        """

        if self.state != 'active':
            raise ValueError("Entity is not 'active'")

        # First, the easy ones (direct copy)
        t = dict(
            ident = self.ident,
            revision = self.revision,
            title = self.title,
            release_date = self.release_date,
            release_type = self.release_type,
            release_status = self.release_status,
            language = self.language,
            doi = self.doi,
            pmid = self.pmid,
            pmcid = self.pmcid,
            isbn13 = self.isbn13,
            core_id = self.core_id,
            wikidata_qid = self.wikidata_qid
        )

        container = self.container
        container_is_kept = False
        if container:
            t['publisher'] = container.publisher
            t['container_name'] = container.name
            t['container_issnl'] = container.issnl
            container_extra = container.extra
            if container_extra:
                t['container_is_oa'] = container_extra.get('is_oa')
                container_is_kept = container_extra.get('is_kept', False)
                t['container_is_longtail_oa'] = container_extra.get('is_longtail_oa')
        else:
            t['publisher'] = self.publisher

        files = self.files or []
        t['file_count'] = len(files)
        in_wa = False
        in_ia = False
        t['file_pdf_url'] = None
        for f in files:
            is_pdf = 'pdf' in f.get('mimetype', '')
            for url in f.get('urls', []):
                if url.get('rel', '') == 'webarchive':
                    in_wa = True
                if '//web.archive.org/' in url['url'] or '//archive.org/' in url['url']:
                    in_ia = True
                    if is_pdf:
                        t['file_pdf_url'] = url['url']
                if not t['file_pdf_url'] and is_pdf:
                    t['file_pdf_url'] = url['url']
        t['file_in_webarchive'] = in_wa
        t['file_in_ia'] = in_ia

        extra = self.extra or dict()
        if extra:
            t['in_shadow'] = extra.get('in_shadow')
            if extra.get('grobid') and extra['grobid'].get('is_longtail_oa'):
                t['container_is_longtail_oa'] = True
        t['any_abstract'] = bool(self.abstracts)
        t['is_kept'] = container_is_kept or extra.get('is_kept', False)

        t['ref_count'] = len(self.refs or [])
        t['contrib_count'] = len(self.contribs or [])
        contrib_names = []
        for c in (self.contribs or []):
            if c.raw_name:
                contrib_names.append(c.raw_name)
        t['contrib_names'] = contrib_names
        return t
