import requests
from bs4 import BeautifulSoup
import json
import time
from datetime import datetime

class GratkaScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'pl,en-US;q=0.9,en;q=0.8',
            'Referer': 'https://gratka.pl/',
            'Origin': 'https://gratka.pl'
        }
        self.api_url = "https://gratka.pl/api/v1/listings"

    def search(self, criteria: dict) -> list:
        """Wyszukuje oferty używając API Gratki"""
        print("\n🔍 Rozpoczynam wyszukiwanie z parametrami:")
        for key, value in criteria.items():
            print(f"   - {key}: {value}")

        # Przygotowanie parametrów API
        params = {
            'category': 'mieszkania',
            'location': criteria.get('city', ''),
            'sort': 'default',
            'page': 1,
            'limit': 24,  # standardowa liczba wyników na stronie
        }

        if 'price_max' in criteria:
            params['price.to'] = criteria['price_max']
        if 'rooms_min' in criteria:
            params['rooms.from'] = criteria['rooms_min']
        if 'surface_min' in criteria:
            params['surface.from'] = criteria['surface_min']

        all_results = []
        page = 1

        try:
            while True:
                print(f"\n📄 Pobieram stronę {page}...")
                params['page'] = page
                
                response = requests.get(
                    self.api_url,
                    headers=self.headers,
                    params=params
                )
                response.raise_for_status()
                
                data = response.json()
                
                # Zapisz surowe dane do pliku (do debugowania)
                with open(f"gratka_api_response_page_{page}.json", 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                print(f"💾 Zapisano surowe dane API do pliku gratka_api_response_page_{page}.json")

                if 'data' not in data or not data['data']:
                    print("⚠️ Brak więcej wyników")
                    break

                offers = self._parse_offers(data['data'])
                all_results.extend(offers)
                
                print(f"✅ Znaleziono {len(offers)} ofert na stronie {page}")

                # Sprawdź czy jest następna strona
                if not data.get('hasNextPage', False) or page >= 3:
                    break

                page += 1
                time.sleep(2)  # Przerwa między zapytaniami

        except requests.RequestException as e:
            print(f"\n❌ Błąd podczas pobierania danych: {e}")
            return all_results

        return all_results

    def _parse_offers(self, offers_data: list) -> list:
        """Przetwarza dane ofert z API"""
        results = []
        for offer in offers_data:
            try:
                offer_data = {
                    'title': offer.get('title', 'Brak tytułu'),
                    'price': f"{offer.get('price', {}).get('value', 'Cena nieznana')} {offer.get('price', {}).get('currency', 'PLN')}",
                    'location': f"{offer.get('location', {}).get('city', '')} - {offer.get('location', {}).get('district', '')}",
                    'url': f"https://gratka.pl{offer.get('url', '')}",
                    'surface': f"{offer.get('surface', {}).get('value', 'b/d')} m²",
                    'rooms': offer.get('rooms', 'b/d')
                }
                results.append(offer_data)
            except Exception as e:
                print(f"⚠️ Błąd podczas parsowania oferty: {str(e)}")
                continue
        return results

def main():
    # Kryteria wyszukiwania
    criteria = {
        'city': 'warszawa',
        # 'price_max': 500000,
        # 'rooms_min': 2,
        # 'surface_min': 38
    }
    
    scraper = GratkaScraper()
    results = scraper.search(criteria)
    
    if not results:
        print("\n❌ Nie znaleziono żadnych ofert!")
        return
        
    print(f"\n📊 Znaleziono łącznie {len(results)} ofert")
    
    # Wyświetl pierwsze 5 wyników
    for i, offer in enumerate(results[:5], 1):
        print(f"\n🏠 Oferta {i}:")
        print(f"Tytuł: {offer['title']}")
        print(f"Cena: {offer['price']}")
        print(f"Lokalizacja: {offer['location']}")
        print(f"Powierzchnia: {offer['surface']}")
        print(f"Liczba pokoi: {offer['rooms']}")
        print(f"Link: {offer['url']}")
    
    # Zapisz wszystkie wyniki do pliku
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"gratka_results_{timestamp}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"\n💾 Zapisano wyniki do pliku: {filename}")

if __name__ == "__main__":
    main()