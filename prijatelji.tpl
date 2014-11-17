%if not obstaja:
    <hl>Oseba ne obstaja</hl>
%else:
    %if prijatelji:
    <hl>Prijatelji osebe {{ ime }} {{ priimek }} so: </hl>
    <ul>
    %for (i, p) in prijatelji:
    <li>{{i}} {{p}}</li>
    %end
    </ul>

%else:
<hl>Oseba {{ ime }} {{ priimek }} nima prijatelji</hl>
%end
%end