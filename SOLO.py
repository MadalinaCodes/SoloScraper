#
#
#  Basic for scraping data from static pages
#
# ------ IMPORTANT! ------
# if you need return soup object:
# you cand import from __utils -> GetHtmlSoup
# if you need return regex object:
# you cand import from __utils ->
# ---> get_data_with_regex(expression: str, object: str)
#
# Company ---> SOLO
# Link ------> https://cariere.solo.ro/
#
#
from __utils import (
    GetStaticSoup,
    get_county,
    get_job_type,
    Item,
    UpdateAPI,
)


def scraper():
    '''
    ... scrape data from SOLO scraper.
    '''
    soup = GetStaticSoup("https://cariere.solo.ro/")

    job_list = []
    for job in soup.select('div.job-row'):

        # get jobs items from response
        job_list.append(Item(
            job_title=job.select_one('h3.job-title').text.strip(),
            job_link=job.select_one('a.aplica-job')['href'],
            company='SOLO',
            country='Romania',
            county='',
            city='',
            remote='remote',
        ).to_dict())

    return job_list


def main():
    '''
    ... Main:
    ---> call scraper()
    ---> update_jobs() and update_logo()
    '''

    company_name = "SOLO"
    logo_link = "https://cariere.solo.ro/assets/img/logo-black.svg"

    jobs = scraper()

    # uncomment if your scraper done
    UpdateAPI().update_jobs(company_name, jobs)
    UpdateAPI().update_logo(company_name, logo_link)


if __name__ == '__main__':
    main()
