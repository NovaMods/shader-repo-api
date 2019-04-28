# Security

Security is a major consideration for the Shader Repo. There's currently problems in the shader developer community with
devs, especially devs working with MCPE, stealing each other's code and passing it off as their own. The Shader Repo
will have a number of features that try to fight this problem

## Account Verification

By default, all user accounts are unverified. A user will be able to verify their account by proving their identity
through a trusted third-party, such as Twitter or Discord. Verified accounts will have a checkbox next to their name,
similar to Twitter's account verification system

## Official Shaderpacks

Shaderpacks created by a trusted account will be marked as official. This marking will be impossible to recreate in the
title of your shaderpack.

## Protected Shaderpacks

Shaderpacks can be _protected_. The Shader Repo will automatically diff protected shaderpacks against new shaderpacks as
they're uploaded. If a new shaderpack is found to be similar to a protected shaderpack, the Shader Repo will notify the 
shaderpack's author. The original author can chose to disallow the new shaderpack. The author of the new shaderpack can
appeal this decision, which will require manual resolution - probably from someone on the Nova Mods team will have to
make a decision on which shaderpack is the copy, or if a shaderpack was flagged in error

### Caveats

This system makes a massive assumption that the first person to upload a shaderpack is the owner of that code. This will
almost certainly not always be true. I think there are two potential solutions to this problem. The first is to mark a
newer shaderpack as original, and the second is to disable this system entirely. It's possible that there will be so
many flagged shaderpacks, and so many false positives, that the work of sorting them out is too much to handle. I'll 
handle this as it happens
