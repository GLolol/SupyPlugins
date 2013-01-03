###
# Copyright (c) 2012, spline
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('Weather')

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Weather', True)


Weather = conf.registerPlugin('Weather')
conf.registerGlobalValue(Weather,'apiKey', registry.String('', ("""Your wunderground.com API key."""), private=True))
conf.registerChannelValue(Weather,'useImperial', registry.Boolean(True, ("""Use imperial units? Defaults to yes.""")))
conf.registerChannelValue(Weather,'disableANSI', registry.Boolean(False, """Do not display any ANSI (color/bold) for channel."""))
conf.registerChannelValue(Weather,'disableColoredTemp', registry.Boolean(False, """If disableANSI is True, this will color temperatures based on values."""))
conf.registerGlobalValue(Weather,'forecast', registry.Boolean(True, ("""Display forecast in output by default?""")))
conf.registerGlobalValue(Weather,'alerts', registry.Boolean(False, ("""Display alerts by default?""")))
conf.registerGlobalValue(Weather,'almanac', registry.Boolean(False, ("""Display almanac by default?""")))
conf.registerGlobalValue(Weather,'astronomy', registry.Boolean(False, ("""Display astronomy by default?""")))
conf.registerGlobalValue(Weather,'showPressure', registry.Boolean(False, ("""Show pressure in output?""")))
conf.registerGlobalValue(Weather,'showWind', registry.Boolean(False, ("""Show wind in output?""")))
conf.registerGlobalValue(Weather,'lang', registry.String('EN', ("""language to use. See docs for available codes.""")))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=250:
