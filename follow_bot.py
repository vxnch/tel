try:
    import requests, random, string
except ImportError:
    input("Error while importing modules. Please install the modules in requirements.txt")
    exit()
    
class spotify:

    def __init__(self, profile, proxy = None):
        self.session = requests.Session()
        self.profile = profile
        self.proxy = proxy
    
    def register_account(self):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Referer": "https://www.spotify.com/"
        }
        isim = ['Aaron', 'Abbey', 'Abbie', 'Abby', 'Abdul', 'Abe', 'Abel', 'Abigail', 'Abraham', 'Abram', 'Ada', 'Adah', 'Adalberto', 'Adaline', 'Adam', 'Adam', 'Adan', 'Addie', 'Adela', 'Adelaida', 'Adelaide', 'Adele', 'Adelia', 'Adelina', 'Adeline', 'Adell', 'Adella', 'Adelle', 'Adena', 'Adina', 'Adolfo', 'Adolph', 'Adria', 'Adrian', 'Adrian', 'Adriana', 'Adriane', 'Adrianna', 'Adrianne', 'Adrien', 'Adriene', 'Adrienne', 'Afton', 'Agatha', 'Agnes', 'Agnus', 'Agripina', 'Agueda', 'Agustin', 'Agustina', 'Ahmad', 'Ahmed', 'Ai', 'Aida', 'Aide', 'Aiko', 'Aileen', 'Ailene', 'Aimee', 'Aisha', 'Aja', 'Akiko', 'Akilah', 'Al', 'Alaina', 'Alaine', 'Alan', 'Alana', 'Alane', 'Alanna', 'Alayna', 'Alba', 'Albert', 'Albert', 'Alberta', 'Albertha', 'Albertina', 'Albertine', 'Alberto', 'Albina', 'Alda', 'Alden', 'Aldo', 'Alease', 'Alec', 'Alecia', 'Aleen', 'Aleida', 'Aleisha', 'Alejandra', 'Alejandrina', 'Alejandro', 'Alena', 'Alene', 'Alesha', 'Aleshia', 'Alesia', 'Alessandra', 'Aleta', 'Aletha', 'Alethea', 'Alethia', 'Alex', 'Alex', 'Alexa', 'Alexander', 'Alexander', 'Alexandra', 'Alexandria', 'Alexia', 'Alexis', 'Alexis', 'Alfonso', 'Alfonzo', 'Alfred', 'Alfreda', 'Alfredia', 'Alfredo', 'Ali', 'Ali', 'Alia', 'Alica', 'Alice', 'Alicia', 'Alida', 'Alina', 'Aline', 'Alisa', 'Alise', 'Alisha', 'Alishia', 'Alisia', 'Alison', 'Alissa', 'Alita', 'Alix', 'Aliza', 'Alla', 'Allan', 'Alleen', 'Allegra', 'Allen', 'Allen', 'Allena', 'Allene', 'Allie', 'Alline', 'Allison', 'Allyn', 'Allyson', 'Alma', 'Almeda', 'Almeta', 'Alona', 'Alonso', 'Alonzo', 'Alpha', 'Alphonse', 'Alphonso', 'Alta', 'Altagracia', 'Altha', 'Althea', 'Alton', 'Alva', 'Alva', 'Alvaro', 'Alvera', 'Alverta', 'Alvin', 'Alvina', 'Alyce', 'Alycia', 'Alysa', 'Alyse', 'Alysha', 'Alysia', 'Alyson', 'Alyssa', 'Amada', 'Amado', 'Amal', 'Amalia', 'Amanda', 'Amber', 'Amberly', 'Ambrose', 'Amee', 'Amelia', 'America', 'Ami', 'Amie', 'Amiee', 'Amina', 'Amira', 'Ammie', 'Amos', 'Amparo', 'Amy', 'An', 'Ana', 'Anabel', 'Analisa', 'Anamaria', 'Anastacia', 'Anastasia', 'Andera', 'Anderson', 'Andra', 'Andre', 'Andre', 'Andrea', 'Andrea', 'Andreas', 'Andree', 'Andres', 'Andrew', 'Andrew', 'Andria', 'Andy', 'Anette', 'Angel', 'Angel', 'Angela', 'Angele', 'Angelena', 'Angeles', 'Angelia', 'Angelic', 'Angelica', 'Angelika', 'Angelina', 'Angeline', 'Angelique', 'Angelita', 'Angella', 'Angelo', 'Angelo', 'Angelyn', 'Angie', 'Angila', 'Angla', 'Angle', 'Anglea', 'Anh', 'Anibal', 'Anika', 'Anisa', 'Anisha', 'Anissa', 'Anita', 'Anitra', 'Anja', 'Anjanette', 'Anjelica', 'Ann', 'Anna', 'Annabel', 'Annabell', 'Annabelle', 'Annalee', 'Annalisa', 'Annamae', 'Annamaria', 'Annamarie', 'Anne', 'Anneliese', 'Annelle', 'Annemarie', 'Annett', 'Annetta', 'Annette', 'Annice', 'Annie', 'Annika', 'Annis', 'Annita', 'Annmarie', 'Anthony', 'Anthony', 'Antione', 'Antionette', 'Antoine', 'Antoinette', 'Anton', 'Antone', 'Antonetta', 'Antonette', 'Antonia', 'Antonia', 'Antonietta', 'Antonina', 'Antonio', 'Antonio', 'Antony', 'Antwan', 'Anya', 'Apolonia', 'April', 'Apryl', 'Ara', 'Araceli', 'Aracelis', 'Aracely', 'Arcelia', 'Archie', 'Ardath', 'Ardelia', 'Ardell', 'Ardella', 'Ardelle', 'Arden', 'Ardis', 'Ardith', 'Aretha', 'Argelia', 'Argentina', 'Ariana', 'Ariane', 'Arianna', 'Arianne', 'Arica', 'Arie', 'Ariel', 'Ariel', 'Arielle', 'Arla', 'Arlean', 'Arleen', 'Arlen', 'Arlena', 'Arlene', 'Arletha', 'Arletta', 'Arlette', 'Arlie', 'Arlinda', 'Arline', 'Arlyne', 'Armand', 'Armanda', 'Armandina', 'Armando', 'Armida', 'Arminda', 'Arnetta', 'Arnette', 'Arnita', 'Arnold', 'Arnoldo', 'Arnulfo', 'Aron', 'Arron', 'Art', 'Arthur', 'Arthur', 'Artie', 'Arturo', 'Arvilla', 'Asa', 'Asha', 'Ashanti', 'Ashely', 'Ashlea', 'Ashlee', 'Ashleigh', 'Ashley', 'Ashley', 'Ashli', 'Ashlie', 'Ashly', 'Ashlyn', 'Ashton', 'Asia', 'Asley', 'Assunta', 'Astrid', 'Asuncion', 'Athena', 'Aubrey', 'Aubrey', 'Audie', 'Audra', 'Audrea', 'Audrey', 'Audria', 'Audrie', 'Audry', 'August', 'Augusta', 'Augustina', 'Augustine', 'Augustine', 'Augustus', 'Aundrea', 'Aura', 'Aurea', 'Aurelia', 'Aurelio', 'Aurora', 'Aurore', 'Austin', 'Austin', 'Autumn', 'Ava', 'Avelina', 'Avery', 'Avery', 'Avis', 'Avril', 'Awilda', 'Ayako', 'Ayana', 'Ayanna', 'Ayesha', 'Azalee', 'Azucena', 'Azzie', 'Babara', 'Babette', 'Bailey', 'Bambi', 'Bao', 'Barabara', 'Barb', 'Barbar', 'Barbara', 'Barbera', 'Barbie', 'Barbra', 'Bari', 'Barney', 'Barrett', 'Barrie', 'Barry', 'Bart', 'Barton', 'Basil', 'Basilia', 'Bea', 'Beata', 'Beatrice', 'Beatris', 'Beatriz', 'Beau', 'Beaulah', 'Bebe', 'Becki', 'Beckie', 'Becky', 'Bee', 'Belen', 'Belia', 'Belinda', 'Belkis', 'Bell', 'Bella', 'Belle', 'Belva', 'Ben', 'Benedict', 'Benita', 'Benito', 'Benjamin', 'Bennett', 'Bennie', 'Bennie', 'Benny', 'Benton', 'Berenice', 'Berna', 'Bernadette', 'Bernadine', 'Bernard', 'Bernarda', 'Bernardina', 'Bernardine', 'Bernardo', 'Berneice', 'Bernetta', 'Bernice', 'Bernie', 'Bernie', 'Berniece', 'Bernita', 'Berry', 'Berry', 'Bert', 'Berta', 'Bertha', 'Bertie', 'Bertram', 'Beryl', 'Bess', 'Bessie', 'Beth', 'Bethanie', 'Bethann', 'Bethany', 'Bethel', 'Betsey', 'Betsy', 'Bette', 'Bettie', 'Bettina', 'Betty', 'Bettyann', 'Bettye', 'Beula', 'Beulah', 'Bev', 'Beverlee', 'Beverley', 'Beverly', 'Bianca', 'Bibi', 'Bill', 'Billi', 'Billie', 'Billie', 'Billy', 'Billy', 'Billye', 'Birdie', 'Birgit', 'Blaine', 'Blair', 'Blair', 'Blake', 'Blake', 'Blanca', 'Blanch', 'Blanche', 'Blondell', 'Blossom', 'Blythe', 'Bo', 'Bob', 'Bobbi', 'Bobbie', 'Bobbie', 'Bobby', 'Bobby', 'Bobbye', 'Bobette', 'Bok', 'Bong', 'Bonita', 'Bonnie', 'Bonny', 'Booker', 'Boris', 'Boyce', 'Boyd', 'Brad', 'Bradford', 'Bradley', 'Bradly', 'Brady', 'Brain', 'Branda', 'Brande', 'Brandee', 'Branden', 'Brandi', 'Brandie', 'Brandon', 'Brandon', 'Brandy', 'Brant', 'Breana', 'Breann', 'Breanna', 'Breanne', 'Bree', 'Brenda', 'Brendan', 'Brendon', 'Brenna', 'Brent', 'Brenton', 'Bret', 'Brett', 'Brett', 'Brian', 'Brian', 'Briana', 'Brianna', 'Brianne', 'Brice', 'Bridget', 'Bridgett', 'Bridgette', 'Brigette', 'Brigid', 'Brigida', 'Brigitte', 'Brinda', 'Britany', 'Britney', 'Britni', 'Britt', 'Britt', 'Britta', 'Brittaney', 'Brittani', 'Brittanie', 'Brittany', 'Britteny', 'Brittney', 'Brittni', 'Brittny', 'Brock', 'Broderick', 'Bronwyn', 'Brook', 'Brooke', 'Brooks', 'Bruce', 'Bruna', 'Brunilda', 'Bruno', 'Bryan', 'Bryanna', 'Bryant', 'Bryce', 'Brynn', 'Bryon', 'Buck', 'Bud', 'Buddy', 'Buena', 'Buffy', 'Buford', 'Bula', 'Bulah', 'Bunny', 'Burl', 'Burma', 'Burt', 'Burton', 'Buster', 'Byron', 'Caitlin', 'Caitlyn', 'Calandra', 'Caleb', 'Calista', 'Callie', 'Calvin', 'Camelia', 'Camellia', 'Cameron', 'Cameron', 'Cami', 'Camie', 'Camila', 'Camilla', 'Camille', 'Cammie']
        email = ("").join(random.choices(string.ascii_letters + string.digits, k = 8)) + "@gmail.com"
        password = ("").join(random.choices(string.ascii_letters + string.digits, k = 8))
        proxies = None
        if self.proxy != None:
            proxies = {"https": f"http://{self.proxy}"}
        data = f"birth_day=1&birth_month=01&birth_year=1970&collect_personal_info=undefined&creation_flow=&creation_point=https://www.spotify.com/uk/&displayname={isim[random.randint(200,600)]}&email={email}&gender=neutral&iagree=1&key=a1e486e2729f46d6bb368d6b2bcda326&password={password}&password_repeat={password}&platform=www&referrer=&send-email=1&thirdpartyemail=0&fb=0"
        try:
            create = self.session.post("https://spclient.wg.spotify.com/signup/public/v1/account", headers = headers, data = data, proxies = proxies)
            if "login_token" in create.text:
                login_token = create.json()['login_token']
                with open("Created.txt", "a") as f:
                    f.write(f'{email}:{password}:{login_token}\n')
                return login_token
            else:
                return None
        except:
            return False

    def get_csrf_token(self):
        try:
            r = self.session.get("https://www.spotify.com/uk/signup/?forward_url=https://accounts.spotify.com/en/status&sp_t_counter=1")
            return r.text.split('csrfToken":"')[1].split('"')[0]
        except:
            return None
        
    def get_token(self, login_token):
        headers = {
            "Accept": "*/*",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRF-Token": self.get_csrf_token(),
            "Host": "www.spotify.com"
        }
        self.session.post("https://www.spotify.com/api/signup/authenticate", headers = headers, data = "splot=" + login_token)
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "app-platform": "WebPlayer",
            "Host": "open.spotify.com",
            "Referer": "https://open.spotify.com/"
        }
        try:
            r = self.session.get(
                "https://open.spotify.com/get_access_token?reason=transport&productType=web_player",
                headers = headers
            )
            return r.json()["accessToken"]
        except:
            return None

    def follow(self):
        if "/user/" in self.profile:
            self.profile = self.profile.split("/user/")[1]
        if "?" in self.profile:
            self.profile = self.profile.split("?")[0]
        login_token = self.register_account()
        if login_token == None:
            return None, "while registering, ratelimit"
        elif login_token == False:
            if self.proxy == None:
                return None, f"unable to send request on register"
            return None, f"bad proxy on register {self.proxy}"
        auth_token = self.get_token(login_token)
        if auth_token == None:
            return None, "while getting auth token"
        headers = {
            "accept": "application/json",
            "Accept-Encoding": "gzip, deflate, br",
            "accept-language": "en",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            "app-platform": "WebPlayer",
            "Referer": "https://open.spotify.com/",
            "spotify-app-version": "1.1.52.204.ge43bc405",
            "authorization": "Bearer {}".format(auth_token),
        }
        try:
            self.session.put(
                "https://api.spotify.com/v1/me/following?type=user&ids=" + self.profile,
                headers = headers
            )
            return True, None
        except:
            return False, "while following"

#Developed by https://github.com/7zx
