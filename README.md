## Data Dictionary

| Column Name | Data Type | Description | Business Relevance |
| :--- | :--- | :--- | :--- |
| `user_id` | Integer | Unique identifier assigned to each customer account. | Crucial for tracking user history, mapping journeys, and checking retention. |
| `age` | Integer | The age of the customer in years. | Allows demographics-focused marketing and targeted product curation. |
| `gender` | Categorical | Self-reported gender of the user (e.g., Male, Female). | Used for segmenting marketing campaigns and predicting purchasing trends. |
| `device_type` | Categorical | The hardware/OS used to browse (e.g., Mobile, Desktop). | Helps UI/UX teams optimize platform performance for the most popular devices. |
| `time_on_site` | Float | Total duration (in minutes) spent on the e-commerce platform. | Represents initial user engagement; drop-offs indicate potential page frictions. |
| `pages_viewed` | Integer | Total number of individual pages visited during the session. | High page counts with zero purchases indicate a messy navigation setup. |
| `previous_purchases` | Integer | Number of historical orders successfully placed by the user. | Key metric for calculating Customer Lifetime Value (CLV). |
| `cart_items` | Integer | Number of items added to the virtual cart during the session. | Essential for optimizing cart abandonment campaigns. |
| `discount_seen` | Binary (0/1) | Indicates whether a promotional discount banner was displayed. | Measures the direct impact and conversion power of promotional campaigns. |
| `ad_clicked` | Binary (0/1) | Tracks whether the user landed on the site via an advertisement. | Measures the effectiveness and return on investment (ROI) of marketing spend. |
| `returning_user` | Binary (0/1) | Identifies if the user has visited the platform previously. | Used to balance new user acquisition costs with cheaper user retention. |
| `avg_session_time` | Float | Historical average duration of the user's web sessions. | Establishes a baseline behavior profile for personalizing user experiences. |
| `bounce_rate` | Float | Percentage of single-page sessions with zero interaction. | Higher bounce rates alert tech teams to slow load speeds or poor landing pages. |
| `purchase` | Binary (0/1) | Target Variable: 1 if an order was placed; 0 if they left without buying. | The ultimate metric to measure business revenue and growth success. |
