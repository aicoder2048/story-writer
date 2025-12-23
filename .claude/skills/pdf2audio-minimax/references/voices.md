# MiniMax Chinese Mandarin Voices

## Voice Selection Guide

### By Content Type

| Content Type | Recommended Voice | Voice ID |
|-------------|-------------------|----------|
| Audiobook (male narrator) | Gentleman | `Chinese (Mandarin)_Gentleman` |
| Audiobook (female narrator) | Soft Girl | `Chinese (Mandarin)_Soft_Girl` |
| Children's story | Cute Spirit | `Chinese (Mandarin)_Cute_Spirit` |
| News/Formal | News Anchor | `Chinese (Mandarin)_News_Anchor` |
| Podcast/Radio | Radio Host | `Chinese (Mandarin)_Radio_Host` |
| Educational | Kind-hearted Elder | `Chinese (Mandarin)_Kind-hearted_Elder` |
| Young adult fiction | Gentle Youth | `Chinese (Mandarin)_Gentle_Youth` |
| Romance | Sweet Lady | `Chinese (Mandarin)_Sweet_Lady` |

### By Voice Character

#### Male Voices
| Name | Voice ID | Character |
|------|----------|-----------|
| Gentleman | `Chinese (Mandarin)_Gentleman` | Mature, authoritative, warm |
| News Anchor | `Chinese (Mandarin)_News_Anchor` | Professional, clear, formal |
| Male Announcer | `Chinese (Mandarin)_Male_Announcer` | Broadcast style, clear |
| Radio Host | `Chinese (Mandarin)_Radio_Host` | Friendly, conversational |
| Reliable Executive | `Chinese (Mandarin)_Reliable_Executive` | Professional, trustworthy |
| Unrestrained Young Man | `Chinese (Mandarin)_Unrestrained_Young_Man` | Energetic, free-spirited |
| Southern Young Man | `Chinese (Mandarin)_Southern_Young_Man` | Regional accent, friendly |
| Gentle Youth | `Chinese (Mandarin)_Gentle_Youth` | Soft, youthful, kind |
| Humorous Elder | `Chinese (Mandarin)_Humorous_Elder` | Warm, humorous, elderly |
| Kind-hearted Elder | `Chinese (Mandarin)_Kind-hearted_Elder` | Wise, warm, grandfatherly |
| Sincere Adult | `Chinese (Mandarin)_Sincere_Adult` | Honest, straightforward |
| Gentle Senior | `Chinese (Mandarin)_Gentle_Senior` | Calm, experienced |
| Straightforward Boy | `Chinese (Mandarin)_Straightforward_Boy` | Direct, youthful |
| Pure-hearted Boy | `Chinese (Mandarin)_Pure-hearted_Boy` | Innocent, young |
| Stubborn Friend | `Chinese (Mandarin)_Stubborn_Friend` | Persistent, loyal |

#### Female Voices
| Name | Voice ID | Character |
|------|----------|-----------|
| Soft Girl | `Chinese (Mandarin)_Soft_Girl` | Gentle, soothing, feminine |
| Sweet Lady | `Chinese (Mandarin)_Sweet_Lady` | Warm, pleasant, refined |
| Cute Spirit | `Chinese (Mandarin)_Cute_Spirit` | Lively, youthful, playful |
| Warm Girl | `Chinese (Mandarin)_Warm_Girl` | Friendly, approachable |
| Crisp Girl | `Chinese (Mandarin)_Crisp_Girl` | Clear, bright voice |
| Mature Woman | `Chinese (Mandarin)_Mature_Woman` | Sophisticated, experienced |
| Wise Women | `Chinese (Mandarin)_Wise_Women` | Knowledgeable, calm |
| Lyrical Voice | `Chinese (Mandarin)_Lyrical_Voice` | Musical, expressive |
| Warm Bestie | `Chinese (Mandarin)_Warm_Bestie` | Friendly, casual |
| HK Flight Attendant | `Chinese (Mandarin)_HK_Flight_Attendant` | Professional, polite |
| Kind-hearted Antie | `Chinese (Mandarin)_Kind-hearted_Antie` | Motherly, caring |
| Intellectual Girl | `Chinese (Mandarin)_IntellectualGirl` | Smart, articulate |
| Warm-hearted Girl | `Chinese (Mandarin)_Warm_HeartedGirl` | Kind, emotional |
| Laid-back Girl | `Chinese (Mandarin)_Laid_BackGirl` | Relaxed, casual |
| Explorative Girl | `Chinese (Mandarin)_ExplorativeGirl` | Curious, adventurous |
| Warm-hearted Aunt | `Chinese (Mandarin)_Warm-HeartedAunt` | Caring, mature |
| Bashful Girl | `Chinese (Mandarin)_BashfulGirl` | Shy, soft-spoken |

## Default Voice Selection Logic

When no voice_id is provided, select based on content analysis:

1. **Children's content** (童话、儿童、小朋友) → `Chinese (Mandarin)_Cute_Spirit`
2. **Romance/emotional** (言情、爱情、浪漫) → `Chinese (Mandarin)_Sweet_Lady`
3. **Sci-fi/serious** (科幻、悬疑、历史) → `Chinese (Mandarin)_Gentleman`
4. **News/formal** (新闻、报告、公告) → `Chinese (Mandarin)_News_Anchor`
5. **Default fallback** → `Chinese (Mandarin)_Gentleman`
